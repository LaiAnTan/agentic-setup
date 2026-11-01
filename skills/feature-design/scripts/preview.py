#!/usr/bin/env python3
"""Serve built design pages for the browser preview pane.

    python3 preview.py docs/designs [--port 4319]

Artifact pages have no doctype and rely on the artifact viewer to render
mermaid, and file:// can't open big pages, so this serves each .html with the
doctype, viewport and mermaid the viewer would add. Other files are served as-is.
"""
import argparse
import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

MERMAID_VERSION = "11.6.0"  # cdnjs has no 11.6.8
MERMAID_URL = f"https://cdnjs.cloudflare.com/ajax/libs/mermaid/{MERMAID_VERSION}/mermaid.min.js"

HEAD = (
    '<!doctype html>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
)
MERMAID = (
    f'\n<script src="{MERMAID_URL}"></script>\n'
    "<script>mermaid.initialize({startOnLoad: true, "
    "theme: matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'default'});</script>\n"
)


class Handler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = Path(self.translate_path(self.path))
        if path.suffix != ".html" or not path.is_file():
            return super().send_head()
        page = path.read_text(encoding="utf-8")
        if not page.lstrip().lower().startswith("<!doctype"):
            page = HEAD + page
        if "mermaid.min.js" not in page:
            page += MERMAID
        data = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("directory", nargs="?", default="docs/designs")
    parser.add_argument("--port", type=int, default=4319)
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    if not root.is_dir():
        raise SystemExit(f"No such folder: {root}")
    handler = functools.partial(Handler, directory=str(root))
    print(f"Serving {root} at http://localhost:{args.port}/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", args.port), handler).serve_forever()


if __name__ == "__main__":
    main()

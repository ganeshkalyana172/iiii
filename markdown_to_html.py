"""Simple Markdown-to-HTML converter."""
from pathlib import Path
try:
    import markdown
except ImportError:
    print("Install dependency: python -m pip install markdown")
    raise SystemExit(1)

def main():
    print("Markdown to HTML Converter. Enter Markdown; type END on its own line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip() == "END": break
        lines.append(line)
    body = markdown.markdown("\n".join(lines), extensions=["tables", "fenced_code"])
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Converted Markdown</title><style>body{{font-family:Arial;max-width:900px;margin:40px auto;padding:0 20px;line-height:1.6}}pre{{background:#eee;padding:12px;overflow:auto}}</style></head><body>{body}</body></html>'''
    name = input("Output filename [output.html]: ").strip() or "output.html"
    if not name.lower().endswith(".html"): name += ".html"
    Path(name).write_text(html, encoding="utf-8")
    print("Saved HTML to:", Path(name).resolve())
if __name__ == "__main__": main()

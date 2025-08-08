import os, sys
from pathlib import Path

INPUT_DIR = Path(os.getenv("INPUT_DIR", "/working/input"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/output"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    if not INPUT_DIR.exists():
        print(f"[WARN] Input folder not found: {INPUT_DIR}", file=sys.stderr)

    images = [p for p in INPUT_DIR.rglob("*") if p.suffix.lower() in {".jpg",".jpeg",".png",".bmp",".tif",".tiff"}]
    others = [p for p in INPUT_DIR.rglob("*") if p.is_file() and p.suffix.lower() not in {".jpg",".jpeg",".png",".bmp",".tif",".tiff"}]

    summary = OUTPUT_DIR / "summary.txt"
    with summary.open("w", encoding="utf-8") as f:
        f.write(f"Input folder: {INPUT_DIR}\n")
        f.write(f"Total files (all types): {sum(1 for _ in INPUT_DIR.rglob('*') if _.is_file())}\n")
        f.write(f"Image files counted: {len(images)}\n")
        f.write(f"Other files counted: {len(others)}\n")

    print(f"[OK] Wrote {summary}")
    # exit code 0 indicates success
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

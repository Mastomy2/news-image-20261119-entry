"""Entry for make.fun news-image-20261119.

Copies the pre-rendered poster (image.png, shipped in this repository)
to /output/entry.png. Standard library only, no network, deterministic:
every run writes the same bytes as image.png.
"""

import hashlib
import os
import shutil

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def sha256_of(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("image.png not found next to main.py")
    with open(src, "rb") as f:
        if f.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise ValueError("image.png is not a PNG file")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_hash = sha256_of(src)
    dst_hash = sha256_of(dst)
    assert src_hash == dst_hash, "output differs from image.png"
    assert os.path.getsize(src) == os.path.getsize(dst), "size mismatch"
    print("source sha256: " + src_hash)
    print("sha256: " + dst_hash)
    print("Wrote " + dst + " (" + str(os.path.getsize(dst)) + " bytes)")


if __name__ == "__main__":
    main()

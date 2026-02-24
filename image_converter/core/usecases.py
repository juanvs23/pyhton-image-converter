from pathlib import Path
import logging
from typing import Iterable

from ..adapters.image_service import find_images_recursively, convert_image


def convert_folder(source: Path, target: Path, quality: int = 60, dry_run: bool = False) -> dict:
    """Convert all images found in `source` to `target`.

    Returns a dict with counts of successes and failures.
    """
    # Soportar JPG/JPEG, PNG, TIFF y BMP (mayúsculas/minúsculas)
    extensions = [
        ".jpg",
        ".jpeg",
        ".JPG",
        ".JPEG",
        ".png",
        ".PNG",
        ".tif",
        ".tiff",
        ".TIF",
        ".TIFF",
        ".bmp",
        ".BMP",
    ]
    files = [p for p in find_images_recursively(source, extensions)]

    if not files:
        logging.info("No images found in %s", source)
        return {"success": 0, "fail": 0}

    success = 0
    fail = 0

    for i, src_path in enumerate(files, start=1):
        rel = src_path.relative_to(source)
        out_path = target / rel.with_suffix('.webp')

        if dry_run:
            logging.info("[DRY] %s -> %s", src_path, out_path)
            continue

        ok = convert_image(src_path, out_path, quality)
        if ok:
            success += 1
        else:
            fail += 1

    return {"success": success, "fail": fail}

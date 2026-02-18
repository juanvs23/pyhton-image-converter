from pathlib import Path
import logging
from typing import Iterable

from ..adapters.image_service import find_images_recursively, convert_image


def convert_folder(source: Path, target: Path, quality: int = 60, dry_run: bool = False) -> dict:
    """Convertir todas las imágenes encontradas en `source` a `target`.

    Retorna un dict con conteo de éxitos y fallos.
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
    archivos = [p for p in find_images_recursively(source, extensions)]

    if not archivos:
        logging.info("No se encontraron imágenes en %s", source)
        return {"success": 0, "fail": 0}

    success = 0
    fail = 0

    for i, origen in enumerate(archivos, start=1):
        rel = origen.relative_to(source)
        salida = target / rel.with_suffix('.webp')

        if dry_run:
            logging.info("[DRY] %s -> %s", origen, salida)
            continue

        ok = convert_image(origen, salida, quality)
        if ok:
            success += 1
        else:
            fail += 1

    return {"success": success, "fail": fail}

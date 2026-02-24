from pathlib import Path
import logging
from PIL import Image


def _has_transparency(img: Image.Image) -> bool:
    # Detección básica de transparencia compatible con PNG (RGBA/LA) y paletas con transparencia (P)
    if img.mode in ("RGBA", "LA"):
        return True
    if img.mode == "P" and "transparency" in img.info:
        return True
    return False


def convert_image(path_in: Path, path_out: Path, quality: int) -> bool:
    try:
        path_out.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(path_in) as img:
            if _has_transparency(img):
                if img.mode != "RGBA":
                    img = img.convert("RGBA")
            else:
                if img.mode != "RGB":
                    img = img.convert("RGB")
            # Guardar sin metadata: hacer una copia y limpiar info conocida
            img_to_save = img.copy()
            for meta_key in ("exif", "icc_profile", "dpi", "transparency"):
                if meta_key in img_to_save.info:
                    img_to_save.info.pop(meta_key, None)

            img_to_save.save(path_out, "WEBP", quality=quality)
        logging.info("Converted: %s -> %s", path_in, path_out)
        return True
    except Exception:
        logging.exception("Error converting %s", path_in)
        return False


def find_images_recursively(source: Path, extensions):
    for ext in extensions:
        yield from source.rglob(f"*{ext}")

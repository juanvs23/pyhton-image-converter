from pathlib import Path
import argparse
import logging
from logging.handlers import RotatingFileHandler

from .core.usecases import convert_folder


def setup_logging(log_file: str, level: str = "INFO"):
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger = logging.getLogger()
    logger.setLevel(numeric_level)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)
    ch.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(ch)

    # Rotating file handler
    fh = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8")
    fh.setLevel(numeric_level)
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(fh)


def main(argv: list = None):
    parser = argparse.ArgumentParser(description="Convertir JPG/JPEG a WebP manteniendo estructura de carpetas")
    parser.add_argument("--source", "-s", help="Carpeta origen (por defecto: 'source' en el proyecto)")
    parser.add_argument("--target", "-t", default="target", help="Carpeta destino (por defecto: 'target')")
    parser.add_argument("--quality", "-q", type=int, default=60, help="Calidad WebP (1-100)")
    parser.add_argument("--dry-run", action="store_true", help="Mostrar qué se convertiría sin escribir archivos")
    parser.add_argument("--log-file", default="logs/conversion.log", help="Archivo de log (por defecto: logs/conversion.log)")
    parser.add_argument("--log-level", default="INFO", help="Nivel de logging (DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args(argv)

    cwd = Path.cwd()
    if args.source:
        src = Path(args.source)
    else:
        src = cwd / "source"
        if not src.exists():
            src.mkdir(parents=True, exist_ok=True)
            print(f"No se encontró la carpeta 'source'. Se ha creado en: {src}")

    setup_logging(args.log_file, args.log_level)

    if not src.exists() or not src.is_dir():
        logging.error("Error: la carpeta fuente '%s' no existe o no es un directorio.", src)
        raise SystemExit(1)

    dst = Path(args.target)
    dst.mkdir(parents=True, exist_ok=True)

    result = convert_folder(src, dst, quality=args.quality, dry_run=args.dry_run)
    logging.info("Proceso finalizado. Éxitos: %d. Fallos: %d.", result.get("success", 0), result.get("fail", 0))

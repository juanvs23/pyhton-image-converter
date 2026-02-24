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
    parser = argparse.ArgumentParser(description="Convert JPG/JPEG to WebP preserving folder structure")
    parser.add_argument("--source", "-s", help="Source folder (default: 'source' in the project)")
    parser.add_argument("--target", "-t", default="target", help="Target folder (default: 'target')")
    parser.add_argument("--quality", "-q", type=int, default=60, help="WebP quality (1-100)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be converted without writing files")
    parser.add_argument("--log-file", default="logs/conversion.log", help="Log file (default: logs/conversion.log)")
    parser.add_argument("--log-level", default="INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR)")
    args = parser.parse_args(argv)

    cwd = Path.cwd()
    if args.source:
        source_path = Path(args.source)
    else:
        source_path = cwd / "source"
        if not source_path.exists():
            source_path.mkdir(parents=True, exist_ok=True)
            print(f"'source' folder not found. Created at: {source_path}")

    setup_logging(args.log_file, args.log_level)

    if not source_path.exists() or not source_path.is_dir():
        logging.error("Error: source folder '%s' does not exist or is not a directory.", source_path)
        raise SystemExit(1)

    target_path = Path(args.target)
    target_path.mkdir(parents=True, exist_ok=True)

    result = convert_folder(source_path, target_path, quality=args.quality, dry_run=args.dry_run)
    logging.info("Process finished. Successes: %d. Failures: %d.", result.get("success", 0), result.get("fail", 0))

# Image Converter

Pequeño script para convertir imágenes JPG/JPEG a WebP manteniendo la estructura de carpetas.

```markdown
# Image Converter

Small script to convert JPG/JPEG images to WebP while preserving folder structure.

**Status:** 0.1.0

## Requirements
- Python 3.8+ (development environment detected: Python 3.12.3)
- Dependencies in [requirements.txt](requirements.txt)

Detected environment in the project:

- Python: 3.12.3
- Pillow: 12.1.1

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage (CLI)

Show help:

```bash
python3 main.py --help
```

Example: list operations (dry-run) using the default `source` folder:

```bash
python3 main.py --dry-run
```

Force source folder (relative or absolute) in dry-run:

```bash
python3 main.py --source "./path/to/my/images" --dry-run
```

Run actual conversion (uses `source/` and `target/` by default):

```bash
python3 main.py
```

Specify source, target and quality:

```bash
python3 main.py -s "/path/source" -t "/path/target" -q 80
```

Main options:
- `--source`, `-s`: Source folder. If not provided, `source/` in the project is used (it will be created if missing).
- `--target`, `-t`: Target folder. Default is `target/`.
- `--quality`, `-q`: WebP quality (1-100). Default is 60.
- `--dry-run`: Do not write files, just list the actions.

## Behavior
- The script recursively walks the source folder and converts files with `.jpg` and `.jpeg` extensions (case-insensitive).
- The relative folder structure is preserved in the target folder; output files use the `.webp` extension.
- Transparency is preserved when present; otherwise images are converted to `RGB`.

- By default the script writes a log to `logs/conversion.log`. You can change the path with `--log-file`.
- The `logs/` directory is included in `.gitignore` to avoid committing logs to the repository.

Logging details:

- By default the script writes logs to `logs/conversion.log` using a `RotatingFileHandler`.
- Available flags:
	- `--log-file <path>`: log file to use (default `logs/conversion.log`).
	- `--log-level <level>`: logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- The log file rotates at 5MB and keeps up to 5 backups.

## Supported formats

- JPG / JPEG (case-insensitive).
- PNG (basic support). PNG images with an alpha channel preserve transparency; otherwise they are converted to `RGB`.

Limitations:
- Animated images (e.g., animated GIFs or APNG) are not supported by default — they require specific handling.

- TIFF / TIF (raster image files) are supported; metadata is not preserved.
- BMP (Bitmap) files are supported; metadata is not preserved.

Note about metadata:
- The process DOES NOT preserve metadata such as EXIF, ICC profile or DPI. This avoids leaking extra information and reduces the resulting file size.

## Architecture and modularization

The project follows a Clean Architecture-inspired structure to separate responsibilities:

- `image_converter/cli.py`: Command-line interface and logging setup.
- `image_converter/core/usecases.py`: High-level logic (conversion orchestrator).
- `image_converter/adapters/image_service.py`: Low-level operations (I/O, open/save images).
- `main.py`: Minimal entrypoint that delegates to `image_converter.cli.main()`.

Benefits:
- More testable and maintainable code.
- Clear separation between business logic and implementation details.

How to run using the new structure:

```bash
# Traditional entrypoint
python3 main.py --dry-run

# Or run the module directly
python3 -m image_converter.cli --help
```

## Versioning
Semantic versioning (SemVer) is used. The current project version is **0.1.0** (Initial release).

Additional environment info (detected in `.venv`):

- Python: 3.12.3
- Pillow: 12.1.1

SemVer format: `MAJOR.MINOR.PATCH`
- Breaking changes: increment `MAJOR`.
- Added features: increment `MINOR`.
- Bug fixes / small improvements: increment `PATCH`.

## Changelog
See [CHANGELOG.md](CHANGELOG.md).

## Notes
- If you work in a path that contains spaces, wrap paths in quotes.
- For large batches, choose an appropriate `--quality` and monitor disk space.

```

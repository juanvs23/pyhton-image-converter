# Changelog

All notable changes to this project are documented in this file.

Format: keep entries per version, with date and listed changes.

## [0.1.0] - 2026-02-18
- Initial release.
  - Refactored `main.py` into a CLI using `argparse`.
  - Recursive folder traversal and preservation of structure in `target/`.
  - Transparency handling and conversion to WebP.
  - `--dry-run` option to simulate conversions.
  - `requirements.txt` includes `pillow`.

## [0.1.1] - 2026-02-18
- Added logging system.
  - Added `RotatingFileHandler` writing by default to `logs/conversion.log`.
  - Added CLI flags: `--log-file` and `--log-level`.
  - Added `logs/` to `.gitignore` to avoid committing logs.

## [0.2.0] - 2026-02-18
- Modularization and reorganization following Clean Architecture.
  - New package `image_converter/` with modules `cli`, `core` and `adapters`.
  - `main.py` converted to a lightweight entrypoint delegating to `image_converter.cli.main()`.
  - Separation of concerns: `usecases` orchestrates conversion; `adapters` perform I/O.
  - Documentation updated (`README.md`, `PROJECT_CONTEXT.md`) to reflect the new architecture.

## [0.2.1] - 2026-02-18
- Added support for PNG files.
  - `.png` files are detected and converted preserving transparency when present.
  - Documentation updated: `README.md`, `PROJECT_CONTEXT.md`.
  - Note: animations (GIF/APNG) are not supported.

## [0.2.2] - 2026-02-18
- Added support for TIFF and BMP.
  - Support for `.tif`, `.tiff`, `.bmp` (case-insensitive) in recursive search.
  - Conversions do not preserve metadata (EXIF, ICC profile, DPI) by default.
  - Documentation updated: `README.md`, `PROJECT_CONTEXT.md`.

## How to write future entries
- Add a new section for the new version at the top.
- Use format: `## [X.Y.Z] - YYYY-MM-DD` and list changes.

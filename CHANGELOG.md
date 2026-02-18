# Changelog

Todos los cambios notables en este proyecto se documentan en este archivo.

Formato: Mantener entradas por versión, con fecha y cambios listados.

## [0.1.0] - 2026-02-18
- Release inicial.
  - Refactorización de `main.py` a CLI con `argparse`.
  - Recorrido recursivo de carpetas y preservación de estructura en `target/`.
  - Manejo de transparencia y conversión a WebP.
  - Opción `--dry-run` para simular conversiones.
  - `requirements.txt` incluye `pillow`.

## [0.1.1] - 2026-02-18
- Añadido sistema de logging.
  - Se añadió `RotatingFileHandler` que escribe por defecto en `logs/conversion.log`.
  - Añadidos flags CLI: `--log-file` y `--log-level`.
  - Se añadió `logs/` a `.gitignore` para evitar subir registros.

## [0.2.0] - 2026-02-18
- Modularización y reorganización siguiendo Clean Architecture.
  - Nuevo paquete `image_converter/` con módulos `cli`, `core` y `adapters`.
  - `main.py` convertido a entrypoint ligero que delega en `image_converter.cli.main()`.
  - Separación de responsabilidades: `usecases` orquesta la conversión; `adapters` realizan I/O.
  - Actualización de documentación (`README.md`, `PROJECT_CONTEXT.md`) para reflejar la nueva arquitectura.

## [0.2.1] - 2026-02-18
- Añadido soporte para archivos PNG.
  - Se detectan y convierten archivos `.png` preservando transparencia cuando existe.
  - Documentación actualizada: `README.md`, `PROJECT_CONTEXT.md`.
  - Nota: animaciones (GIF/APNG) no están soportadas.

## [0.2.2] - 2026-02-18
- Añadido soporte para TIFF y BMP.
  - Soporte para `.tif`, `.tiff`, `.bmp` (mayúsculas/minúsculas) en la búsqueda recursiva.
  - Las conversiones no preservan metadata (EXIF, ICC profile, DPI) por defecto.
  - Documentación actualizada: `README.md`, `PROJECT_CONTEXT.md`.

## Cómo escribir futuras entradas
- Añadir una nueva sección con la nueva versión en la parte superior.
- Usar formato: `## [X.Y.Z] - YYYY-MM-DD` y listar cambios.

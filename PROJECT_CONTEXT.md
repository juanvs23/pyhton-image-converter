# Contexto del proyecto — Image Converter

Este archivo proporciona contexto y directrices para futuros desarrollos automatizados o asistidos por IA.

## Resumen
- Nombre: Image Converter
- Propósito: Convertir imágenes JPG/JPEG a WebP preservando la estructura de carpetas.
- Versión actual: 0.1.0

## Objetivos principales
- Proveer una herramienta CLI simple, segura y predecible para convertir imágenes a WebP.
- Mantener la estructura relativa de carpetas en la salida (`target/`).
- Evitar operaciones destructivas por defecto (usar `--dry-run` para revisar antes).

## Estructura del repositorio
- `main.py` — Script principal (CLI) que recorre recursivamente la carpeta fuente y convierte archivos.
 - `main.py` — Entrypoint mínimo que delega en `image_converter.cli`.
 - `image_converter/` — Paquete modular que contiene:
	 - `cli.py` — Interfaz de línea de comandos y configuración de logging.
	 - `core/usecases.py` — Lógica de aplicación (orquestador de conversiones).
	 - `adapters/image_service.py` — Operaciones de I/O y conversión de imágenes.
- `requirements.txt` — Dependencias (actual: `pillow==12.1.1`).
- `source/` — Carpeta por defecto para colocar imágenes de origen.
- `target/` — Carpeta destino donde se escriben las imágenes convertidas.
- `README.md`, `CHANGELOG.md`, `PROJECT_CONTEXT.md` — Documentación del proyecto.

## Dependencias y entorno
- Requiere Python 3.8+.
- Crear entorno virtual y ejecutar `pip install -r requirements.txt`.

Entorno detectado en el proyecto (`.venv`):

- Python: 3.12.3
- Pillow: 12.1.1

Nota: la IA debe preferir usar el intérprete en `.venv/bin/python` cuando ejecute comandos o pruebas para replicar el entorno del proyecto.

## Comandos CLI principales
- `python3 main.py --help` — Mostrar ayuda.
- `python3 main.py --dry-run` — Listar conversiones sin escribir archivos.
- `python3 main.py -s <ruta_origen> -t <ruta_destino> -q <calidad>` — Ejecutar conversión real.

## Comportamiento importante (para la IA)
- El script debe preservar la estructura de carpetas relativa de `source` dentro de `target`.
- No borrar ni sobrescribir archivos existentes sin confirmación expresa del usuario.
- Usar siempre rutas absolutas o bien tratar correctamente rutas con espacios (usar comillas en CLI).
- Soportar `jpg` y `jpeg` en mayúsculas y minúsculas.
- Mantener transparencia cuando exista; convertir a `RGB` cuando no exista.
 - Soportar `jpg`, `jpeg` y `png` en mayúsculas y minúsculas.
 - Mantener transparencia cuando exista; convertir a `RGB` cuando no exista.
 - Nota: formatos animados (GIF/APNG) no son soportados por defecto.
 - Soportar `jpg`, `jpeg`, `png`, `tif`/`tiff` y `bmp` en mayúsculas y minúsculas.
 - Mantener transparencia cuando exista; convertir a `RGB` cuando no exista.
 - No preservar metadata (EXIF/ICC/DPI) en las conversiones por defecto.
 - Nota: formatos animados (GIF/APNG) no son soportados por defecto.
 - Mantener transparencia cuando exista; convertir a `RGB` cuando no exista.
 - Se añadió un sistema de logging basado en `logging` con `RotatingFileHandler` que escribe por defecto en `logs/conversion.log`.
	 - El logger rota a 5MB y mantiene 5 backups.
	 - La IA debe respetar que `logs/` está ignorado por git y no subir registros.
	 - Exponer y documentar los flags `--log-file` y `--log-level` cuando se propongan cambios relacionados con ejecución.

## Convenciones de código / estilo
- Seguir PEP8 para Python.
- Preferir `pathlib.Path` para manipulación de rutas.
- Evitar efectos secundarios al importar módulos (no ejecutar conversión en import).
- Añadir `argparse` y mensajes claros para el usuario.

## Reglas para cambios por IA
Cuando la IA realice cambios o proponga parches:
- Explicar brevemente el propósito del cambio.
- Priorizar pruebas locales: recomendar `--dry-run` antes de ejecutar conversiones reales.
- No modificar nombres de carpetas por defecto (`source`, `target`) a menos que el usuario solicite explícitamente.
- No eliminar archivos originales salvo petición explícita.

## Tareas comunes y ejemplos para la IA
- Ejecutar `dry-run` y devolver la lista de archivos que se convertirían.
- Añadir soporte para más formatos (PNG, TIFF) con flag opcional.
- Implementar logging en fichero con niveles `INFO`/`ERROR`.

## Mantenibilidad
- Versionado: SemVer. Incrementar `MINOR` al añadir funcionalidades, `PATCH` para correcciones.
- Mantener `CHANGELOG.md` actualizado.

## Contacto / mantenedor
- Usuario en repo: juanvs23 (propietario local). Para cambios importantes, solicitar confirmación a través del entorno.

## Notas adicionales
- El proyecto está pensado para ejecutarse localmente; no debe incorporar llamadas de red externas automáticas.
- Evitar añadir dependencias innecesarias sin justificación.

## Notas sobre la modularización (Clean Architecture)
- La lógica de negocio debe vivir en `image_converter/core` y no depender de detalles de I/O.
- Los adaptadores (`image_converter/adapters`) implementan detalles concretos (lectura/escritura de ficheros, formatos).
- La capa CLI orquesta ejecución y configura dependencias (logger, rutas).
- Añadir tests centrados en `core/usecases.py` usando mocks para adaptadores.

## Recomendaciones para la IA al modificar código
- Mantener la separación entre capas: no mover lógica de negocio a `adapters` ni I/O a `core`.
- Documentar cualquier cambio de interfaz pública en `image_converter` y actualizar `README.md` y `CHANGELOG.md`.

## Regla de idioma

A partir de ahora, las siguientes reglas se aplican al proyecto y deben ser respetadas por cualquier cambio automatizado o asistido por IA:

- Los archivos `README.md` y `CHANGELOG.md` deben estar en inglés.
- Las variables, nombres de funciones y mensajes de usuario dentro del código fuente deben utilizar inglés.
- El archivo `PROJECT_CONTEXT.md` queda exento de esta regla y seguirá redactado en español.

La IA debe aplicar estas reglas al realizar traducciones o refactorizaciones. Registrar cualquier cambio de variables en el changelog.

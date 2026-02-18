# Image Converter

Pequeño script para convertir imágenes JPG/JPEG a WebP manteniendo la estructura de carpetas.

**Estado:** 0.1.0

## Requisitos
- Python 3.8+ (entorno de desarrollo detectado: Python 3.12.3)
- Dependencias en [requirements.txt](requirements.txt)

Entorno detectado en el proyecto:

- Python: 3.12.3
- Pillow: 12.1.1

Instalar dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso (CLI)

Mostrar ayuda:

```bash
python3 main.py --help
```

Ejemplo: listado (dry-run) usando la carpeta por defecto `source`:

```bash
python3 main.py --dry-run
```

Forzar carpeta fuente (ruta relativa o absoluta) en dry-run:

```bash
python3 main.py --source "./ruta/a/mis/imagenes" --dry-run
```

Ejecutar conversión real (usa `source/` y `target/` por defecto):

```bash
python3 main.py
```

Especificar carpeta fuente, destino y calidad:

```bash
python3 main.py -s "/ruta/source" -t "/ruta/target" -q 80
```

Parámetros principales:
- `--source`, `-s`: Carpeta origen. Si no se indica, usa `source/` en el proyecto (se crea si no existe).
- `--target`, `-t`: Carpeta destino. Por defecto `target/`.
- `--quality`, `-q`: Calidad WebP (1-100). Por defecto 60.
- `--dry-run`: No escribe archivos, solo lista las acciones.

## Comportamiento
- El script recorre recursivamente la carpeta fuente y convierte los archivos con extensión `.jpg` y `.jpeg` (también mayúsculas).
- La estructura relativa de carpetas se preserva en la carpeta destino; los archivos se guardan con la extensión `.webp`.
- Se preserva la transparencia cuando la imagen la tiene; en caso contrario se fuerza a `RGB`.

- El script crea un registro (log) en `logs/conversion.log` por defecto. Puedes cambiar la ruta con `--log-file`.
- El directorio `logs/` está en `.gitignore` para evitar subir registros al repositorio.

Logging (detalles):

- Por defecto el script escribe logs en `logs/conversion.log` usando un `RotatingFileHandler`.
- Flags disponibles:
	- `--log-file <ruta>`: archivo de log a usar (por defecto `logs/conversion.log`).
	- `--log-level <nivel>`: nivel de logging (`DEBUG`, `INFO`, `WARNING`, `ERROR`).
- El archivo de log rota a 5MB y mantiene hasta 5 archivos de respaldo.

## Arquitectura y modularización

El proyecto fue reorganizado siguiendo una estructura inspirada en Clean Architecture para separar responsabilidades:

- `image_converter/cli.py`: Interfaz de línea de comandos y configuración de logging.
- `image_converter/core/usecases.py`: Lógica de alto nivel (orquestador de la conversión).
- `image_converter/adapters/image_service.py`: Operaciones de bajo nivel (I/O, apertura y guardado de imágenes).
- `main.py`: Entrypoint mínimo que delega en `image_converter.cli.main()`.

Beneficios:
- Código más testeable y mantenible.
- Separación clara entre lógica de negocio y detalles de implementación.

Cómo ejecutar usando la nueva estructura:

```bash
# Entrypoint tradicional
python3 main.py --dry-run

# O ejecutar el módulo directamente
python3 -m image_converter.cli --help
```

## Versionado
Se utiliza versionado semántico (SemVer). La versión actual del proyecto es **0.1.0** (Initial release).

Información adicional del entorno (detectada en `.venv`):

- Python: 3.12.3
- Pillow: 12.1.1

Formato SemVer: `MAJOR.MINOR.PATCH`
- Cambios incompatibles: incrementar `MAJOR`.
- Añadidos/funcionalidades: incrementar `MINOR`.
- Correcciones/pequeñas mejoras: incrementar `PATCH`.

## Changelog
Ver [CHANGELOG.md](CHANGELOG.md).

## Notas
- Si trabajas en un entorno con espacios en la ruta del proyecto, pasa rutas entre comillas.
- Para convertir grandes volúmenes, usa `--quality` adecuada y monitoriza espacio en disco.

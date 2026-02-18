"""Paquete principal para Image Converter (modularizado).
Exponer la función `main()` desde el módulo `cli`.
"""
from .cli import main  # re-export

__all__ = ["main"]

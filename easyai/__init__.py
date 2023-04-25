"""Easy SDWebUI API - Easy API for SDWebUI, forked from mix1009/sdwebuiapi"""
from .image import HiResUpscaler, Upscaler
from .interfaces import (
    ControlNetInterface,
    ControlNetUnit,
    InstructPix2PixInterface,
    ModelKeywordInterface,
)
from .main import EasyAPI

__version__ = "0.1.2"

__all__ = [
    "__version__",
    "EasyAPI",
    "ModelKeywordInterface",
    "InstructPix2PixInterface",
    "ControlNetInterface",
    "ControlNetUnit",
    "Upscaler",
    "HiResUpscaler",
]

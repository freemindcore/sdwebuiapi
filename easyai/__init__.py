"""Easy SDWebUI API - Easy API for SDWebUI, forked from mix1009/sdwebuiapi"""
from .controlnet import ControlNetUnit
from .interfaces import (
    ControlNetInterface,
    InstructPix2PixInterface,
    ModelKeywordInterface,
)
from .main import EasyAI, EasyAPI, easyai
from .upscaler import HiResUpscaler, Upscaler

__version__ = "0.1.4rc1"

__all__ = [
    "easyai",
    "EasyAI",
    "EasyAPI",
    "ModelKeywordInterface",
    "InstructPix2PixInterface",
    "ControlNetInterface",
    "ControlNetUnit",
    "Upscaler",
    "HiResUpscaler",
]

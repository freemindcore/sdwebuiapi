"""Easy SDWebUI API - Easy API for SDWebUI, forked from mix1009/sdwebuiapi"""
from .controlnet import ControlNetUnit
from .interfaces import (
    ControlNetInterface,
    InstructPix2PixInterface,
    ModelKeywordInterface,
)
from .main import EasyAPI
from .upscaler import HiResUpscaler, Upscaler


class EasyAI(EasyAPI):
    def __init__(self):
        super().__init__(
            host="127.0.0.1",
            port=80,
            use_https=False,
        )


easyai = EasyAI()

__version__ = "0.1.2"

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

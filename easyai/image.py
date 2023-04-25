import base64
import io
from enum import Enum

from PIL import Image


def b64_img(image: Image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = "data:image/png;base64," + str(
        base64.b64encode(buffered.getvalue()), "utf-8"
    )
    return img_base64


def raw_b64_img(image: Image):
    # XXX controlnet only accepts RAW base64 without headers
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = str(base64.b64encode(buffered.getvalue()), "utf-8")
    return img_base64


class Upscaler(str, Enum):
    none = "None"
    Lanczos = "Lanczos"
    Nearest = "Nearest"
    LDSR = "LDSR"
    BSRGAN = "BSRGAN"
    ESRGAN_4x = "ESRGAN_4x"
    R_ESRGAN_General_4xV3 = "R-ESRGAN General 4xV3"
    ScuNET_GAN = "ScuNET GAN"
    ScuNET_PSNR = "ScuNET PSNR"
    SwinIR_4x = "SwinIR 4x"


class HiResUpscaler(str, Enum):
    none = "None"
    Latent = "Latent"
    LatentAntialiased = "Latent (antialiased)"
    LatentBicubic = "Latent (bicubic)"
    LatentBicubicAntialiased = "Latent (bicubic antialiased)"
    LatentNearest = "Latent (nearist)"
    LatentNearestExact = "Latent (nearist-exact)"
    Lanczos = "Lanczos"
    Nearest = "Nearest"
    ESRGAN_4x = "ESRGAN_4x"
    LDSR = "LDSR"
    ScuNET_GAN = "ScuNET GAN"
    ScuNET_PSNR = "ScuNET PSNR"
    SwinIR_4x = "SwinIR 4x"

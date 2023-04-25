import base64
import io

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

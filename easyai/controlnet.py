from PIL import Image

from .image import raw_b64_img


# https://github.com/Mikubill/sd-webui-controlnet
class ControlNetUnit:
    def __init__(
        self,
        input_image: Image = None,
        mask: Image = None,
        module: str = "none",
        model: str = "None",
        weight: float = 1.0,
        resize_mode: str = "Resize and Fill",
        lowvram: bool = False,
        processor_res: int = 512,
        threshold_a: float = 0.1,
        threshold_b: float = 0.1,
        guidance: float = 1.0,
        guidance_start: float = 0.0,
        guidance_end: float = 1.0,
        control_mode: int = 0,
        pixel_perfect: bool = False,
        guessmode: int = None,  # deprecated: use control_mode
    ):
        self.input_image = input_image
        self.mask = mask
        self.module = module
        self.model = model
        self.weight = weight
        self.resize_mode = resize_mode
        self.lowvram = lowvram
        self.processor_res = processor_res
        self.threshold_a = threshold_a
        self.threshold_b = threshold_b
        self.guidance = guidance
        self.guidance_start = guidance_start
        self.guidance_end = guidance_end
        if guessmode:
            print(
                "ControlNetUnit guessmode is deprecated. Please use control_mode instead."
            )
            control_mode = guessmode
        self.control_mode = control_mode
        self.pixel_perfect = pixel_perfect

    def to_dict(self):
        return {
            "input_image": raw_b64_img(self.input_image) if self.input_image else "",
            "mask": raw_b64_img(self.mask) if self.mask is not None else None,
            "module": self.module,
            "model": self.model,
            "weight": self.weight,
            "resize_mode": self.resize_mode,
            "lowvram": self.lowvram,
            "processor_res": self.processor_res,
            "threshold_a": self.threshold_a,
            "threshold_b": self.threshold_b,
            "guidance": self.guidance,
            "guidance_start": self.guidance_start,
            "guidance_end": self.guidance_end,
            "control_mode": self.control_mode,
            "pixel_perfect": self.pixel_perfect,
        }

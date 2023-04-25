from dataclasses import dataclass


@dataclass
class ApiResult:
    images: list
    parameters: dict
    info: dict

    @property
    def image(self):
        return self.images[0]

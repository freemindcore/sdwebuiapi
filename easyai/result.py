from dataclasses import dataclass


@dataclass
class APIResult:
    images: list
    parameters: dict
    info: dict

    @property
    def image(self):
        return self.images[0]

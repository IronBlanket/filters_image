from PIL import Image


class Filter:
    def apply_to_pixel(self, r, g, b):
        pass

    def apply_to_image(self, img: Image.Image) -> object:
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))

                new_pixel = self.apply_to_pixel(r, g, b)

                img.putpixel((i, j), new_pixel)
        return img


class RedFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        r = min(255, r + 100)
        pixel = (r, g, b)
        return pixel


class GreenFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        g = min(255, g + 100)
        pixel = (r, g, b)
        return pixel


class BlueFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        b = min(255, b + 100)
        pixel = (r, g, b)
        return pixel


class InversedFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        r = 255 - r
        g = 255 - g
        b = 255 - b
        pixel = (r, g, b)
        return pixel


class DarkFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        r = max(0, r - 100)
        g = max(0, g - 100)
        b = max(0, b - 100)
        pixel = (r, g, b)
        return pixel


class LigthFilter(Filter):

    def apply_to_pixel(self, r, g, b):
        r = min(255, r + 100)
        g = min(255, g + 100)
        b = min(255, b + 100)
        pixel = (r, g, b)
        return pixel

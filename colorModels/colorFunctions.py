import colorsys

from PIL import Image


def rgb_to_cmyk(rgb):
    r, g, b = rgb
    c = 1 - r / 255.0
    m = 1 - g / 255.0
    y = 1 - b / 255.0
    k = min(c, m, y)
    if k == 1:
        return 0, 0, 0, 1
    c = (c - k) / (1 - k)
    m = (m - k) / (1 - k)
    y = (y - k) / (1 - k)
    return c, m, y, k


def cmyk_to_rgb(cmyk):
    c, m, y, k = cmyk
    r = int(255 * (1 - c) * (1 - k))
    g = int(255 * (1 - m) * (1 - k))
    b = int(255 * (1 - y) * (1 - k))
    return r, g, b


def rgb_to_hsl(rgb):
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return int(h * 360), s, l


def hsl_to_rgb(hsl):
    h, s, l = hsl
    r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
    return int(r * 255), int(g * 255), int(b * 255)


def convert_hsl_to_rgb(pixels):
    modified_pixels = []

    for px in pixels:
        px = hsl_to_rgb(px)
        modified_pixels.append(px)

    return modified_pixels


def cmyk_modify_saturation(cmyk, delta_s, color):
    c, m, y, k = cmyk
    if color == "Cyan":
        c *= delta_s
    elif color == "Yellow":
        y *= delta_s
    elif color == "Both":
        c *= delta_s
        y *= delta_s
    return int(round(c)), m, int(round(y)), k


def hsl_modify_saturation(hsl, delta_s, color):
    h, s, l = hsl

    if color == "Cyan":
        if 210 < h < 270:
            s = delta_s
    elif color == "Yellow":
        if 30 < h < 90:
            s = delta_s
    elif color == "Both":
        if 30 < h < 90 or 210 < h < 270:
            s = delta_s

    return h, s, l


def modify_saturation_hsl(pixels_hsl, delta_s, color):
    modified_pixels = []

    for px in pixels_hsl:
        px = hsl_modify_saturation(px, delta_s, color)
        modified_pixels.append(px)

    return modified_pixels


def modify_saturation_cmyk(pixels_cmyk, delta_s, color):
    modified_pixels = []

    for px in pixels_cmyk:
        px = cmyk_modify_saturation(px, delta_s, color)
        modified_pixels.append(px)

    return modified_pixels

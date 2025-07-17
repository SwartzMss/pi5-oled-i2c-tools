import time
from typing import Tuple

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306, sh1106
from luma.core.render import canvas
from PIL import ImageFont


# ---------- 工具函数 ---------- #
def _line_height(font: ImageFont.FreeTypeFont) -> int:
    """
    返回字体行高，兼容 Pillow 新旧版本。

    Pillow 9.x: 仍有 font.getsize
    Pillow10.x: 推荐 font.getmetrics()
    """
    ascent, descent = font.getmetrics()      # 两个值均为正
    return ascent + descent                  # 行高≈上升+下降


# ---------- OLED 初始化 ---------- #
def init_display(
    i2c_port: int = 1,
    i2c_address: int = 0x3C,
    *,
    driver: str = "sh1106",                  # "sh1106" 或 "ssd1306"
    width: int = 128,
    height: int = 64,
    rotate: int = 0,
):
    """Initialize and return the OLED device."""
    serial = i2c(port=i2c_port, address=i2c_address)

    if driver.lower() == "sh1106":
        device = sh1106(serial, width=width, height=height, rotate=rotate)
    else:
        device = ssd1306(serial, width=width, height=height, rotate=rotate)

    return device


# ---------- 显示函数 ---------- #
def show_message(device, message: str, duration: float = 2.0):
    """Display a single‑line message."""
    font = ImageFont.load_default()
    with canvas(device) as draw:
        draw.text((0, 0), message, font=font, fill=255)
    time.sleep(duration)


def show_environment(
    device,
    *,
    temperature: float = 25.0,
    humidity: float = 40.0,
    duration: float = 2.0,
    font_path: str = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    font_size: int = 12,
):
    """Display temperature & humidity in Chinese on two lines."""
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        font = ImageFont.load_default()

    line_h = _line_height(font)

    with canvas(device) as draw:
        draw.text((0, 0),  f"温度：{temperature:.1f}℃", font=font, fill=255)
        draw.text((0, line_h), f"湿度：{humidity:.1f}%", font=font, fill=255)

    time.sleep(duration)

import time
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306, sh1106
from luma.core.render import canvas
from PIL import ImageFont

def init_display(
    i2c_port: int = 1,
    i2c_address: int = 0x3C,
    *,
    driver: str = "ssd1306",
    width: int = 128,
    height: int = 64,
    rotate: int = 0,
):
    """Initialize and return the OLED device."""
    serial = i2c(port=i2c_port, address=i2c_address)
    if driver == "sh1106":
        device = sh1106(serial, width=width, height=height, rotate=rotate)
    else:
        device = ssd1306(serial, width=width, height=height, rotate=rotate)
    return device


def show_message(device, message: str, duration: float = 2.0):
    """Display a single-line message."""
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
    """Display temperature and humidity in Chinese on two lines."""
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        font = ImageFont.load_default()
    with canvas(device) as draw:
        draw.text((0, 0), f"温度：{temperature:.1f}℃", font=font, fill=255)
        draw.text((0, 16), f"湿度：{humidity:.1f}%", font=font, fill=255)
    time.sleep(duration)

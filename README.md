# pi5-oled-i2c-tools

树莓派 Pi5 使用 I2C 接口驱动 OLED 显示屏的示例代码。

## 依赖安装

```bash
pip install luma.oled Pillow
```

如需显示中文，请先安装中文字体：

```bash
sudo apt-get install fonts-wqy-zenhei
```

确认 I²C 已启用

```bash
sudo raspi-config
```

## 接线说明

| OLED 引脚 | Raspberry Pi5 引脚 |
|-----------|-------------------|
| VCC       | 1 (3.3V)          |
| GND       | 9 (GND)           |
| SCL       | 5 (GPIO3 / SCL1)  |
| SDA       | 3 (GPIO2 / SDA1)  |
连接完成后，开启 I2C 接口并重启树莓派即可。

## 示例

- `main.py`：显示默认的温度和湿度信息（例如 25°C，40%）。 屏幕上会以中文显示温度和湿度。

运行示例：

```bash
python main.py
```

示例设备图片：

<img src="doc/device.jpg" alt="Device" width="300" />

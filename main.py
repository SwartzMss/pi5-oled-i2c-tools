from oled_display import init_display, show_environment


def main():
    device = init_display(i2c_port=10, i2c_address=0x3C, driver="sh1106")
    # 默认演示温度 25 摄氏度，湿度 40%
    show_environment(device, temperature=25.0, humidity=40.0)


if __name__ == "__main__":
    main()

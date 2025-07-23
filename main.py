from oled_display import init_display, show_environment, show_time, show_smiley
import argparse


def main():
    parser = argparse.ArgumentParser(description="OLED demo")
    parser.add_argument("--time", action="store_true", help="display current time")
    parser.add_argument("--smile", action="store_true", help="display blinking smiley")
    args = parser.parse_args()

    device = init_display(i2c_port=1, i2c_address=0x3C, driver="sh1106")

    if args.smile:
        show_smiley(device)
    elif args.time:
        show_time(device)
    else:
        # 默认演示温度 25 摄氏度，湿度 40%
        show_environment(device, temperature=25.0, humidity=40.0)


if __name__ == "__main__":
    main()

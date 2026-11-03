from datetime import datetime


def main() -> None:
    now = datetime.now()
    blue = "\033[34m"
    reset = "\033[0m"
    print(f"{blue}{now:%I}{reset}:{now:%M %p}")


if __name__ == "__main__":
    main()
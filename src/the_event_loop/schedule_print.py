import asyncio
import datetime


def print_now() -> None:
    print(datetime.datetime.now())


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.call_soon(print_now)
    loop.call_soon(print_now)
    loop.run_until_complete(asyncio.sleep(5))


if __name__ == "__main__":
    main()

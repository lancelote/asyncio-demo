import asyncio
import datetime


def print_now() -> None:
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end="")
        print_now()
        await asyncio.sleep(0.5)


def main() -> None:
    asyncio.run(asyncio.wait_for(keep_printing(), 10))


if __name__ == '__main__':
    main()

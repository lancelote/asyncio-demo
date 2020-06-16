import asyncio
import datetime


def print_now() -> None:
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.5)


async def main() -> None:
    try:
        await asyncio.wait_for(keep_printing("Hey"), 10)
    except asyncio.TimeoutError:
        print("oops, time's up")


if __name__ == '__main__':
    asyncio.run(main())

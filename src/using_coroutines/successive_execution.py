import asyncio
import datetime


def print_now() -> None:
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.5)


async def async_main() -> None:
    await keep_printing("First")
    await keep_printing("Second")
    await keep_printing("Third")


if __name__ == '__main__':
    asyncio.run(async_main())

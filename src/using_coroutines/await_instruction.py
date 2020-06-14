import asyncio
import datetime


async def callback(i: int) -> None:
    print(i, datetime.datetime.now())
    await asyncio.sleep(i)


async def main() -> None:
    await callback(1)
    await callback(2)
    await callback(3)


if __name__ == '__main__':
    asyncio.run(main())

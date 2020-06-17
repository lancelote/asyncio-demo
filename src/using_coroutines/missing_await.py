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
    kp = keep_printing("Hey")
    waiter = asyncio.wait_for(kp, 3)
    try:
        waiter
    except asyncio.TimeoutError:
        print("oops, tim's up!")


if __name__ == '__main__':
    # define for a better stacktrace
    # PYTHONASYNCIODEBUG=1
    # PYTHONTRACEMALLOC=1
    asyncio.run(async_main())

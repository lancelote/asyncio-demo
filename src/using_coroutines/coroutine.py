import asyncio
import datetime
import inspect


def print_now() -> None:
    print(datetime.datetime.now())


async def print3times() -> None:
    for _ in range(3):
        print_now()
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    coro1 = print3times()
    coro2 = print3times()

    print(type(print3times))
    print(type(coro1))
    print(type(coro2))

    # Async functions are not awaitable
    print(f"is async function awaitable: {inspect.isawaitable(print3times)}")

    # Coroutines are awaitable
    print(f"is coroutine awaitable: {inspect.isawaitable(coro1)}")

    try:
        asyncio.run(print3times)
    except ValueError:
        print("cannot run async function")

    asyncio.run(coro1)

    try:
        asyncio.run(coro1)
    except RuntimeError:
        print("cannot reuse already awaited coroutine")

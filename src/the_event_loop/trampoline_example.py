import asyncio
import datetime
import random
from asyncio import AbstractEventLoop


def print_now() -> None:
    print(datetime.datetime.now())


def trampoline(loop: AbstractEventLoop, name: str = "") -> None:
    print(name, end=" ")
    print_now()
    loop.call_later(random.random(), trampoline, loop, name)
    loop.call_later(random.random(), trampoline, loop, name)


def main() -> None:
    loop = asyncio.get_event_loop()

    loop.call_soon(trampoline, loop, "First")
    loop.call_soon(trampoline, loop, "Second")
    loop.call_soon(trampoline, loop, "Third")

    loop.call_later(2, loop.stop)
    loop.run_forever()


if __name__ == '__main__':
    main()

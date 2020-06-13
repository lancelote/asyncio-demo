import asyncio


def hog() -> int:
    print("start computing ...")
    total = 0
    for i in range(10_000):
        for j in range(1_000):
            total += i + j
    print("done computing")
    return total


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.call_later(5, hog)
    loop.call_later(10, loop.stop)
    loop.run_forever()


if __name__ == '__main__':
    main()

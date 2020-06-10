import asyncio


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(5))


if __name__ == "__main__":
    main()

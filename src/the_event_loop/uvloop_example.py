import asyncio

import uvloop


def main():
    uvloop.install()
    loop = asyncio.get_event_loop()
    print(loop)


if __name__ == '__main__':
    main()

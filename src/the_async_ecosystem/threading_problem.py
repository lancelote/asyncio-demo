import time
import threading
from typing import Mapping


class Mayhem(threading.Thread):
    def __init__(self, map: Mapping[str, int]) -> None:
        super().__init__()
        self.map = map

    def run(self) -> None:
        for key, value in self.map.items():
            time.sleep(value)


def main() -> None:
    d = {"k1": 1, "k2": 2, "k3": 3}
    m = Mayhem(d)
    m.start()
    d["k4"] = 4


if __name__ == '__main__':
    main()

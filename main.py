import random
import time

from crc import (
    crc8,
    crc8_table_mirrored,
    crc8_with_table,
    generate_crc8_table,
    generate_mirrored_crc8_table,
)


def generate_strings(k=1000):
    result = ["0" if random.random() > 0.5 else "1" for _ in range(k)]
    return "".join(result)


def main():
    print("generating tables...")
    start = time.time_ns()
    table = generate_crc8_table()
    end = time.time_ns()
    print("table generated in", (end - start) / 1e6)

    start = time.time_ns()
    mirrored_table = generate_mirrored_crc8_table()
    end = time.time_ns()
    print("mirrored table generated in", (end - start) / 1e6)

    print("generating data...")
    data = [generate_strings() for _ in range(100000)]
    results = [0, 0, 0]

    print("testing...")
    for d in data:
        start = time.time()
        crc8(d)
        end = time.time()
        results[0] += end - start

    for d in data:
        start = time.time()
        crc8_with_table(d, table)
        end = time.time()
        results[1] += end - start

    for d in data:
        start = time.time()
        crc8_table_mirrored(d, mirrored_table)
        end = time.time()
        results[2] += end - start

    print([r * 1000 for r in results])
    print([r * 1000 / len(data) for r in results])


if __name__ == "__main__":
    main()

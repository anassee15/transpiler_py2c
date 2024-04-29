def test(a: int, b: int) -> int:
    while b > 0:
        b = b - 1
        print(b)

    return a + b


def test2() -> int:
    return 1


if __name__ == "__main__":
    a = test(10, 10) + 2

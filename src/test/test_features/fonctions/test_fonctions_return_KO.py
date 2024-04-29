def test(a: int, b: str) -> int:
    while a > 0:
        a = a - 1

    return b + 5.2


if __name__ == "__main__":
    print(test(5, "3"))

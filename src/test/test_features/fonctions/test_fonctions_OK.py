def fo(x: int, y: int) -> int:
    return x + y


def foo(x: float, y: float) -> None:
    print(x + y)


if __name__ == "__main__":
    a = fo(5, 1)
    b = fo(2 + 5, 2)
    foo(2.3, 4.5)
    print(fo(fo(2, 3), 2))

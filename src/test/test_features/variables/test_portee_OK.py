global_var = 10


def fo(x: int, y: int) -> int:
    global global_var
    global_var = 100
    return x + y


if __name__ == "__main__":
    a = 5
    b = 10
    c = fo(a, b)
    d = "not used"

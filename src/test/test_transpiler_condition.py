def max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    if max(1, 2) == 2:
        print('ok')
    elif 2 > 3:
        print('wtf ?')
    elif 3 > 4:
        print('...')
    else:
        print('nope')

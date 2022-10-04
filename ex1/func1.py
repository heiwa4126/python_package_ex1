def func1(a, b):
    return add(a, b) * sub(a, b)


if __name__ == "__main__":
    from add import add
    from sub import sub

    print(func1(2, 1))

if __package__:
    from .add import add
    from .sub import sub


def func1(a, b):
    print(__name__)
    print(__package__)
    return add(a, b) * sub(a, b)


if __name__ == "__main__":
    from add import add
    from sub import sub

    print(func1(2, 1))

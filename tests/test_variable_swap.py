def test_swap():
    print("\n")
    a = 10
    b = 5
    print_vars(a, b)
    a, b = b, a
    print_vars(a, b)

    a = "Hi!"
    b = "Justin!!"
    print_vars(a, b)
    a, b = b, a
    print_vars(a, b)


def print_vars(a, b):
    print(f"a={a}, b={b}")

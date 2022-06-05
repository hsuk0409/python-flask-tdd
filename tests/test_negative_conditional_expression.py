def test_negative_conditional_expression():
    print("\n")
    num = -1
    print(bin(num))
    print(num.bit_count())
    print(num.bit_length())
    print("\n")
    print(int('10000000', 10))

    if num:
        print("Negative is true!!")

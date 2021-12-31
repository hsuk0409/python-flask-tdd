def test_make_arr_arr():
    print("\n")
    arr_arr = []
    arr = []

    for i in range(0, 4):
        for k in range(0, 10):
            arr.append(k)
        arr_arr.append(arr)

    for i in range(0, 4):
        for k in range(0, 10):
            print(arr_arr[i][k])
        print("\n")

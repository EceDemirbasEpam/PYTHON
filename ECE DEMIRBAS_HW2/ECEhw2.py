def func():
    point1_letters = dict.fromkeys(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], 1)
    print("Letters with a value of 1 \n", point1_letters)

    point2_letters = dict.fromkeys(["D", "G"], 2)
    print("Letters with a value of 2 \n", point2_letters)

    point3_letters = dict.fromkeys(["B", "C", "M", "P"], 3)
    print("Letters with a value of 3 \n", point3_letters)

    point4_letters = dict.fromkeys(["F", "H", "V", "W", "Y"], 4)
    print("Letters with a value of 4 \n", point4_letters)

    point5_letters = dict.fromkeys(["K"], 5)
    print("Letters with a value of 5 \n", point5_letters)

    point8_letters = dict.fromkeys(["J", "X"], 8)
    print("Letters with a value of 8 \n", point8_letters)

    point10_letters = dict.fromkeys(["Q", "Z"], 10)
    print("Letters with a value of 10 \n", point10_letters)

    print("All letters with points are here: \n",
          dict(**point1_letters, **point2_letters, **point3_letters, **point4_letters,
               **point5_letters, **point8_letters, **point10_letters))

func()







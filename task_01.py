def calculate_s(v, v1, t1, t2):
    return v * t1 + (v - v1) * t2


if __name__ == "__main__":

    info = "Yashchenko Yulia km-23"
    print(f"Name and group: {info}")
    v = int(input("Enter v: "))
    v1 = int(input("Enter v1: "))
    t1 = int(input("Enter t1: "))
    t2 = int(input("Enter t2: "))

    s = calculate_s(v, v1, t1, t2)

    print(f"s={s}")



def can_place(r, a):
    if pow(r, 2) - pow(a, 2)/3 < 1e-6:
        return True

    return False


if __name__ == "__main__":
    r = float(input("r = "))
    a = float(input("a = "))

    if can_place(r, a):
        print("Yes")
    else:
        print("No")

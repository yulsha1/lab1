from functions import print_info, read_param


def can_place(r, a):
    epsilon = 1e-6

    if 0 < pow(r, 2) - pow(a, 2) / 3 < epsilon:
        return True

    return False


if __name__ == "__main__":
    print_info(2)

    choice = "y"
    while choice == "y":
        try:
            r = read_param("r = ")
            a = read_param("a = ")
        except ValueError:
            print("Incorrect value")

            choice = input("If you want to continue enter 'y': ")
            if choice != "y":
                break
            continue

        if can_place(r, a):
            print("Yes")
        else:
            print("No")

        choice = input("If you want to continue enter 'y': ")

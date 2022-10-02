from functions import read_param, print_info


def calculate_s(v, v1, t1, t2):
    return v * t1 + (v - v1) * t2


if __name__ == "__main__":
    print_info(1)

    choice = "y"
    while choice == "y":
        try:
            v = read_param("Enter v: ")
            v1 = read_param("Enter v1: ")
            t1 = read_param("Enter t1: ")
            t2 = read_param("Enter t2: ")
        except ValueError:
            print("Incorrect value")

            choice = input("If you want to continue enter 'y': ")
            if choice != "y":
                break
            continue

        s = calculate_s(v, v1, t1, t2)

        print(f"s={s}")
        choice = input("If you want to continue enter 'y': ")

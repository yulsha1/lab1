from functions import print_info


def calculate_f(x):
    if x <= 0:
        return 0

    if x >= 1:
        return pow(x, 4)

    return x


if __name__ == "__main__":
    print_info(3)

    choice = "y"
    while choice == "y":
        try:
            x = float(input("Enter x: "))
        except ValueError:
            print("Incorrect value")
            choice = input("If you want to continue enter 'y': ")
            if choice != "y":
                break
            continue

        f = calculate_f(x)

        print(f"F({x})={f}")

        choice = input("If you want to continue enter 'y': ")

def calculate_f(x):
    if x <= 0:
        return 0

    if x >= 1:
        return pow(x, 4)

    return x


if __name__ == "__main__":
    x = float(input("Enter x: "))
    f = calculate_f(x)
    print(f"F({x})={f}")

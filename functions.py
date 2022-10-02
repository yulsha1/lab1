def read_param(message):
    param = float(input(message))
    if param < 0:
        raise ValueError

    return param


def print_info(task_number):
    info = f"Yashchenko Yulia, KM-23, Task Option: 25, Task Number: {task_number}"
    print(f"Info: {info}")

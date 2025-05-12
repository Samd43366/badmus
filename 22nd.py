def func_1(*args):
    for i, values in enumerate(args):
        print(f"args[{i}] = {values}")

func_1(10, "Hello", 3.14, True)
from mypackage.mylibrary import module


if __name__ == "__main__":
    number_1 = 10
    number_2 = 20

    result = module.add(a=number_1, b=number_2)
    print("Running from mypackage...")
    print(f"{number_1} + {number_2} = {result}")

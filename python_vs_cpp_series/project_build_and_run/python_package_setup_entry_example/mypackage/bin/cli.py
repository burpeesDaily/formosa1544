from mypackage.mylibrary import module


def main():
    number_1 = 10
    number_2 = 20
    result = module.add(a=number_1, b=number_2)
    print("Running from entry...")
    print(f"{number_1} + {number_2} = {result}")

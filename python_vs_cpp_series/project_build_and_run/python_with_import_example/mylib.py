def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    number_1 = 5
    number_2 = 7
    result = add(a=number_1, b=number_2)
    print("Running from the module...")
    print(f"{number_1} + {number_2} = {result}")

def mul_func(param1, param2):
    return param1*param2

def mul_square(param1, param2):
    return param1*param2, param1**param2

def main():
    print(mul_func(5, 2))
    print(type(mul_func(5, 2)))

    print(mul_square(5, 2))
    print(type(mul_square(5, 2)))

if __name__ == "__main__":
    main()
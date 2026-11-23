def evaluate_python_skill(level):
    if level == '상':
        print("아주 열심히 하셨군요")
    elif level == '중':
        print("열심히 하셨군요")
    elif level == '하':
        print("좀 더 열심히 해봅시다")
    else:
        print("상중하로 입력하세요")

def main():
    python_skill = input("파이썬 실력이 어떻게 되나요? (상, 중, 하) : ")
    message = evaluate_python_skill(python_skill)

if __name__ == "__main__":
    main()
def main():
    temp = int(input("오늘 기온은 어떤가요? : "))

    if 30 <= temp:
        print("더워요! 밖에 너무 오래 계시지 마세요")
    elif 10 <= temp <= 30:
        print("외출하기 좋은 날씨네요")
    else:
        print("영하입니다! 추워요!")

if __name__ == '__main__':
    main()
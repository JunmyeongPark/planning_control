# input 기능 제작

if __name__ == "__main__":    
    types = ["<class 'int'>", "<class 'float'>"]
    operators = ['+', '-', '*', '/']
    while (True):
        num1 = input('첫 번째 숫자를 입력하시오 : ')
        if type(num1) not in types:
            print('올바른 값을 입력해주세요.\n')
            continue

        operator = input('연산자를 입력하시오 : ')
        if operator not in operators:
            print('올바른 값을 입력해주세요.\n')
            continue
        
        num2 = input('두 번째 숫자를 입력하시오 : ')
        if type(num2) not in types:
            print('올바른 값을 입력해주세요.\n')
            continue        
        break

    print('finish')
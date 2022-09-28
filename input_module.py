# input 기능 제작
# 두개의 숫자와 연산자를 입력받고, 올바른지 검토한다
# 최종적으로 숫자 두개와 연산자를 리턴한다.

def input_module():
    operators = ['+', '-', '*', '/']
    while (True):
        num1 = input('첫 번째 숫자를 입력하시오 : ')
        if not num1.isdigit():
            print('올바른 값을 입력해주세요.\n')
            continue
        else:
            break

    while (True):        
        operator = input('연산자를 입력하시오 : ')
        if operator not in operators:
            print('올바른 값을 입력해주세요.\n')
            continue
        else:
            break
        
    while (True):    
        num2 = input('두 번째 숫자를 입력하시오 : ')
        if not num2.isdigit():
            print('올바른 값을 입력해주세요.\n')
            continue        
        else:
            break

    return num1, operator, num2

### 테스트용으로 긁어왔습니다.

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

### 코드 시작

data_list = list(input_module())

num_1 = int(data_list[0])
calculator = data_list[1]2
num_2 = int(data_list[2])

if calculator == '*':
    answer = num_1 * num_2

elif calculator == '/':
    answer = num_1 / num_2

## test

print(answer)




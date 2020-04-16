# 메일 내용을 message 변수에 담고
message = """안녕하세요, {0}님
파이썬 수업에 오신걸 환영합니다. 
오늘은 {1}일째 수업입니다. 
남은 기간 즐겁고 행복한 공부가 되길 기원합니다.
"""

while(True):
    # 누구에게 보낼지 이름을 입력을 받아서
    who = input("누구에게 보낼건가요? ")
    date = input("오늘은 몇일째 수업인가요? ")

    # 메일 내용을 완성
    complete_message = message.format(who, date)

    # 출력한다.
    print()
    print("*" * 50)
    print("메일 내용입니다.")
    print("*" * 50)
    print(complete_message)
    
    end = input("끝낼까요? (y/n) ")
    if (end == 'y'):
        print("종료합니다.")
        break

# 메일을 바로 발송
# send_mail(complete_message)
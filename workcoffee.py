# 해결1] 맨윗쪽에 변수 초기화
# 해결2] 반복문while
# 해결3] 논리연산 and or
# 해결4] input() 형변환
# 해결5] if ~ elif ~ else
money, k, n = 0,0,0
message, info = '안내문', ''
pick, select = 0, 0 

money = int(input('금액 입력하세요?'))
while True:
    print()
    print('-------------- 🌻커피 주문 머신🌻 -------------- ')
    print('1.커피(300원) 2.코코아(250원) 3.생수(100원) 4.종료')
    pick  = int(input('메뉴를 선택하세요 >>> '))
    if pick == 4:
        print()
        print('음료 주문 머신을 종료하셨습니다')
        print('잔액은 ', money , '원입니다')
        break
    elif (pick==1 and money<300) or (pick==2 and money<250) :
        print('잔액부족으로 주문을 할수가 없습니다')
    elif pick == 1: #커피주문  
        print('커피 주문 성공입니다')
        money = money-300
        print('커피주문후 잔액은', money,'원') 
    elif pick == 2: #코코주문    
        print('코코아 주문 성공입니다')
        money = money-250  
        print('코코아주문후 잔액은', money,'원') 
    elif pick == 3: #생수주문    
        print('생수 주문 성공입니다')
        money = money-100 
        print('생수주문후 잔액은', money,'원') 
    else:
        print('주문번호를 잘못 입력하셨습니다')

print('카페 프로그램을 종료합니다')






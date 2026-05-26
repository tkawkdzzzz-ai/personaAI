# 10lotto.py
import random
com = random.randint(1,45)    #컴이 발생하는 난수 
print('컴퓨터 난수 ', com)

dice = [1,2,3,4,5,6] 
pick = random.choice(dice)
print('주사위선택숫자 =',pick)

#난수 0.0000 ~ 0.9999  사이 숫자 random()
computer = random.random() #실수형태
print('컴발생숫자 =',computer)

print('🔢로또숫자')
# 1부터 45까지의 숫자 중 6개를 중복 없이 추출
lotto_numbers = random.sample(range(1, 46), 6)
# 보기 좋게 오름차순으로 정렬
lotto_numbers.sort()
print(f"이번 주 행운의 번호는: {lotto_numbers} 입니다!")
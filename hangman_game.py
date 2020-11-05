import time
import csv # csv 호출
import random
import winsound # 사운드 처리

# 처음 인사
name = input("이름을 입력하세요.")
print("안녕하세요!" + name + "님 환영합니다. 행맨게임을 시작합니다.")

print()

time.sleep(1)

print("로딩중입니다...")
print()
time.sleep(1)

# csv 단어 리스트
words = []

# csv 파일로드
with open('./word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기 (csv)
random.shuffle(words) 

q = random.choice(words)

# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 While loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    failed = 0 # 실패횟수

    # 정답 단어 반복
    for char in word:
        if char in guesses: # 정답 단어 내에 추측 문자가 포함되어 있는 경우
            print(char, end = ' ') # 추측 단어 출력
        else:
            print("_", end = ' ') # 틀린 경우 대시로 처리
            failed += 1
    if failed == 0: # 단어 추측이 성공 한 경우
            print()
            print()
            # 성공 사운드
            winsound.PlaySound('./good.wav', winsound.SND_FILENAME)
            print("축하드립니다!" + name + "님 정답입니다.")
            break # while 구문 중단
    print()
    print('힌트 : {}'.format(q[1].strip())) # 추측 단어 문자 단위 입력
    guess = input("단어를 추측해주세요.")
    guesses += guess # 단어 더하기

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1 # 기회 횟수 감소
        print("앗! 틀렸습니다..") # 오류메세지
        print("기회가" , turns , "번 남았습니다. 다시한번 추측해주세요!")

        if turns == 0:
            # 실패 사운드
            winsound.PlaySound('./bad.wav', winsound.SND_FILENAME)
            print("기회가 모두 소진되었습니다. 정답은" + word + "입니다.")

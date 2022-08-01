import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    while is_playing:

        input_num = int(input('1이상 10000이하의 숫자를 입력하세요. : '))

        # try:
        #     input_num = int(input('1이상 10000이하의 숫자를 입력하세요. : '))
        #     break
        # except:
        #     print('숫자만 입력하실 수 있습니다.')

        if input_num > 10000 or input_num < 1:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            continue

        counts += 1

        if input_num > 10000 or input_num < 1:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            continue

        if input_num > answer:
            print('Down!!!')

            continue

        if input_num < answer:
            print('Up!!!')
            continue

        if input_num == answer:
            print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
            restart = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요 : ')
            if restart == 'y':
                is_playing = True
                break
            elif restart == 'n':
                is_playing = False
                print('이용해주셔서 감사합니다. 게임을 종료합니다.')
                break
            else:
                is_playing = False
                print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
                break

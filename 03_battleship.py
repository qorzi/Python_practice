from distutils.log import error
import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    error_site = False
    new_sea = sea
    if 0 < index < 15:
        new_sea[index-1], new_sea[index], new_sea[index+1] = 1, 1, 1
        return error_site, new_sea
    else:
        error_site = True
        return error_site, new_sea


player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    pass
    # 1-1) 플레이어의 배 시작 위치 고르기
    try:
        print()
        idx_num = int(input('배를 위치시킬 시작점을 고르세요. : ')) - 1
        error_site = set_ship(idx_num, player_sea)[0]
        # print(error_site)
        player_sea = set_ship(idx_num, player_sea)[1]
        # print(player_sea)
    except:
        print()
        print('입력된 정보가 없습니다.')
        continue

    if error_site == False:
        print()
        print('위치 선정 완료')
        # print('player 위치: ', player_sea)
        print('-'*90)
        print('< Information Board >')
        print('플레이어의 해역: ', player_sea)
        print('플레이어의 공격 기록: ', player_attacked)
        print('-'*90)
        break
    elif error_site == True:
        print()
        print('-----해당 위치에는 배를 둘 수 없습니다.-----')
        player_sea = [0] * 15
        continue



# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
set_ship(random.choice(range(1,15)), computer_sea)
# print('computer 위치: ',computer_sea)
# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기

# 2. 라운드 진행
attack_round = 0
while True:
    pass
    # 2-1) 플레이어 공격
    # 2-2) 플레이어의 공격 위치 선택
    try:
        print()
        attack_site = int(input('공격할 위치를 선택하세요. : '))
        if not 0 < attack_site < 16:
            print('해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해주세요.')
            continue
        elif player_attacked[attack_site-1] == True:
            print('이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요.')
            continue
    except:
        print()
        print('입력된 정보가 없습니다.')
        continue

    attack_round += 1

    

    # 2-3) 플레이어의 공격이 성공한 경우
    # 2-4) 플레이어의 공격이 실패한 경우
    if computer_sea[attack_site-1] == 1:
        print()
        print(f'< {attack_round}라운드 결과! >')
        print('컴퓨터의 해역 : ', computer_sea)
        print(f'플레이어는 컴퓨터의 해역 {attack_site}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {attack_round}라운드 만에 플레이어의 승리입니다!')
        break
    else:
        player_attacked[attack_site-1] = True


    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    already_attacked_computer = []
    None_attacked_computer = []
    for idx, i in enumerate(computer_attacked):
        if i == True:
            already_attacked_computer += [idx]
        else:
            None_attacked_computer += [idx]
        
    cpu_attack_site = random.choice(None_attacked_computer) + 1

    # 2-6) 컴퓨터의 공격이 성공한 경우
    # 2-7) 컴퓨터의 공격이 실패한 경우
    if player_sea[cpu_attack_site-1] == 1:
        print(f'< {attack_round}라운드 결과! >')
        print(f'플레이어는 컴퓨터의 해역 {attack_site}번째 칸을 공격하였나, 공격에 실패하였습니다!')
        print(f'컴퓨터는 플레이어의 해역 {cpu_attack_site}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.')
        print(f'게임이 종료되었습니다! {attack_round}라운드 만에 컴퓨터의 승리입니다!')
        break
    else:
        computer_attacked[cpu_attack_site-1] = True
        print(f'< {attack_round}라운드 결과! >')
        print(f'플레이어는 컴퓨터의 해역 {attack_site}번째 칸을 공격하였나, 공격에 실패하였습니다!')
        print(f'컴퓨터는 플레이어의 해역 {cpu_attack_site+1}번째 칸을 공격하였으나, 공격에 실패하였습니다!')
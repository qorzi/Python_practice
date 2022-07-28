# 여기에 필요한 모듈을 추가합니다.
from calendar import month
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        pass
        self.number_lines = []
    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        pass
        for _ in range(n):
            self.number_lines += [sorted(random.sample(range(1,46), 6))]
    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year_a, month_a, day_a = Lotto.get_draw_date(draw_number)
        pass
        print('======='*6)
        print(f'             제 {draw_number} 회 로또')
        print('======='*6)
        print(f'추첨일 : {year_a}/{month_a}/{day_a}')
        print('======='*6)

        run_count = 0
        for i in ['A', 'B', 'C', 'D', 'E']:
    
            if run_count >= len(self.number_lines):
                break
            print(f'{i} : {self.number_lines[run_count]}')
            run_count += 1

        

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)
        pass
        print('======='*6)
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('======='*6)

        line_alphas = ['A', 'B', 'C', 'D', 'E']
        for idx, i in enumerate(self.number_lines):
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, i)
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            mess_rank = ''

            if ranking == 1:
                mess_rank = '1등 당첨!'
            elif ranking == 2:
                mess_rank = '2등 당첨!'
            elif ranking == 3:
                mess_rank = '3등 당첨!'
            elif ranking == 4:
                mess_rank = '4등 당첨!'
            elif ranking == 5:
                mess_rank = '5등 당첨!'
            else:
                mess_rank = '낙첨'
                
            print(f'{line_alphas[idx]} : {same_main_counts}개 일치 ({mess_rank})')




    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        pass
        # return year, month, day
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_dict = json.load(lotto_json)
        year = lotto_dict['drwNoDate'][0:4]
        month = lotto_dict['drwNoDate'][5:7]
        day = lotto_dict['drwNoDate'][8:10]
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        pass
        # return main_numbers, bonus_number
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        lotto_dict = json.load(lotto_json)
        main_numbers = [lotto_dict['drwtNo1'], lotto_dict['drwtNo2'], lotto_dict['drwtNo3'], lotto_dict['drwtNo4'], lotto_dict['drwtNo5'], lotto_dict['drwtNo6']]
        bonus_number = lotto_dict['bnusNo']
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        pass
        # return same_main_counts, is_bonus
        same_main_counts = 0
        is_bonus = False

        for i in line:
            if i in main_numbers:
                same_main_counts += 1
            if i == bonus_number:
                is_bonus = True

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        pass
        # return ranking
        ranking = 0

        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5 and is_bonus:
            ranking = 2
        elif same_main_counts == 5:
            ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:
            ranking = -1

        return ranking
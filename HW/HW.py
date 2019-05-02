import random

class Game:
    TYPES = ('камень', 'ножницы', 'бумага', 'ящерица', 'спок')

    def __init__(self):
        counts = 0, 0, 0
        num = 0

    def increase_count(self, n):
        counts[n] += 1

    def round_logic():
        if self.user_choice == self.ii_choice:
            print('Ничья')
            self.increase_count(2)
        elif ((self.user_choice == 'k' and self.ii_choice == 'n')
                 or (self.user_choice == 'n' and self.ii_choice == 'b')
                 or (self.user_choice == 'n' and self.ii_choice == 'y')
                 or (self.user_choice == 'b' and self.ii_choice == 'k')
                 or (self.user_choice == 'b' and self.ii_choice == 's')
                 or (self.user_choice == 'k' and self.ii_choice == 'y')
                 or (self.user_choice == 'k' and self.ii_choice == 'n')
                 or (self.user_choice == 'y' and self.ii_choice == 's')
                 or (self.user_choice == 'y' and self.ii_choice == 'b')
                 or (self.user_choice == 's' and self.ii_choice == 'n')
                 or (self.user_choice == 's' and self.ii_choice == 'k')):
            print('Выигрыш')
            self.increase_count(0)
        else:
            print('Проигрыш')
            self.increase_count(1)

    def round(self):
        while True:
            self.user_choice = input('Камень (k), Ножницы (n), Бумага (b), Ящерица (y), Спок (s)')
            if self.user_choice not in Game.TYPES:
                print('Введите k, n, b, y, s')
            else:
                break

        self.ii_choice = random.choice(Game.TYPES)
        self.round_logic()

        self.num -= 1
        if self.num is 0:
            self.end()

    def end():
        print('Победы - {0}\nПроигрыши - {1}\nНичьи- {2}'.format(*self.counts))

    @staticmethod
    def start():
        while True:
            try:
                n = int(input('Введите количество игр n '))
                return Game(n)
            except ValueError:
                print('Это не число!')

if __name__ == '__main__':
    Game.start()

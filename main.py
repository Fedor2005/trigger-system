import random
from threading import Thread


class Abonent:
    def __init__(self, number):
        self.number = number
        self.account = 0

    def account_change(self, modification):
        self.account += modification


def flow(user, modification):
    user.account_change(modification)
    print('Счет пользователя {} {}.\n '.format(user.number, user.account))


users = []
for i in range(100):
    user = Abonent(i)
    users.append(user)
while True:
    user = random.choice(users)
    modification = random.randint(0, 10000)
    if random.randint(0, 1) == 0:  # смена знака
        modification *= -1
    t = Thread(target=flow, args=(user, modification,))
    t.start()

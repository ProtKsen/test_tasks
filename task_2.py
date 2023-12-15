import random

N_GROUPS = 2
N_PERSONS = 30
IDS = [19, 20]


class Round:

    def __init__(self):
        self.result = None
        self.persons_by_group = N_PERSONS // N_GROUPS

    def generate_groups(self):
        self.result = list(range(1, N_PERSONS + 1))
        random.shuffle(self.result)

    def get_group(self, id):
        if self.result is None:
            self.generate_groups()
        ind = self.result.index(id)
        return ind // self.persons_by_group


class Game:

    def __init__(self, number_rounds):
        self.number_rounds = number_rounds
        self.rounds = []

    def start(self):
        for _ in range(self.number_rounds):
            new_round = Round()
            self.rounds.append(new_round)

    def get_prob_same_group(self, ids):
        if not self.rounds:
            self.start()
        summ = 0
        for round in self.rounds:
            if all([round.get_group(ids[0]) == round.get_group(id_) for id_ in ids]):
                summ +=1
        return summ / self.number_rounds
    

if __name__ == "__main__":

    # численное решение    
    for i in range(1, 6):
        new_game = Game(number_rounds=10 ** i )
        result = new_game.get_prob_same_group(ids=IDS)
        print(f"Количество попыток 1*10^{i}, результат: {result}")

    # аналитическое решение
    prob = 1
    count = 0
    persons_by_group = N_PERSONS // N_GROUPS
    for _ in IDS[1:]:
        count += 1
        prob *= (persons_by_group - count) / (N_PERSONS - count)
    print(f"Аналитический результат: {prob}")

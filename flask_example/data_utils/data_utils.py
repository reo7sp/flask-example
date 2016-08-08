from collections import defaultdict
class DataUtils:
    def __init__(self):
        self.scores = defaultdict(lambda: 0)

    def get_random_girl(self):
        pass

    def get_score(self, girl):
        return self.scores[girl]

    @staticmethod
    def expected_value(first, second):
        return 1/(1+10**((first-second)/400))

    @staticmethod
    def get_koefficient(score):
        if score == 0:
            return 40
        elif score < 2400:
            return 20
        elif score > 2400:
            return 10

    def update_rating(self, girls):
        girls_T = {v: k for k, v in girls.items()}

        girl_first = (girls_T[0], 0)
        girl_second = (girls_T[1], 1)

        # Get rating for first and second girl
        girls_score = (self.get_score(girl_first[0]), self.get_score(girl_second[0]))

        koefficients = (self.get_koefficient(girls_score[0]), self.get_koefficient(girls_score[1]))

        new_rating = (girls_score[0] + koefficients[0] * (girl_first[1] - self.expected_value(girls_score[0], girls_score[1])),
                      girls_score[1] + koefficients[1] * (girl_second[1] - self.expected_value(girls_score[1], girls_score[0])))

        self.scores[girl_first[0]] = new_rating[0]
        self.scores[girl_second[0]] = new_rating[1]
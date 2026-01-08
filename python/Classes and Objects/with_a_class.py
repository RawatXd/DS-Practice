class cricket_player:
    team_size = 11
    def __init__(self,fname,lname,byear,team_name):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.team = team_name
        self.scores = []


    def add_scores(self,score):
     self.scores.append(score)

    def get_average(self):
        return sum(self.scores)/len(self.scores)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is the Cricket Player with {self.team} team."



virat = cricket_player('Virat','Kholi',1984,"India")

virat.add_scores(90)
virat.add_scores(70)
virat.add_scores(60)

# print(virat.first_name)
# print(virat.last_name)
# print(virat.birth_year)
# print(virat.scores)
# print(virat.get_average())

print(virat)


david = cricket_player('David','Warner',1982,"Australia")

david.add_scores(60)
david.add_scores(80)
david.add_scores(40)

# print(david.first_name)
# print(david.last_name)
# print(david.birth_year)
# print(david.scores)
# print(david.get_average())
print(david)
import datetime



class tennis_player:
    team_size = 11
    def __init__(self,fname,lname,byear):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear
        self.aces = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


    def get_average_aces_per_match(self):
        return sum(self.aces)/len(self.aces)

    def add_aces(self,num_aces):
        self.aces.append(num_aces)


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

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def get_average(self):
        return sum(self.scores)/len(self.scores)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is the Cricket Player with {self.team} team."

virat = cricket_player('Virat','Kholi',1984,"India")

virat.add_scores(90)
virat.add_scores(70)
virat.add_scores(60)

print(" Age of Virat Kholi : ",virat.get_age())
print("Average Score of Virat Kholi : ",virat.get_average())

roger = tennis_player('Roger',"Federer",1981)
roger.add_aces(5)
roger.add_aces(7)
print(" Age of Roger Federer : ",roger.get_age())

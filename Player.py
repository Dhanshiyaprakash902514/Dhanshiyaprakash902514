class Player(object):
    def _init_(self, name, age, skills, style=None):
        self.name = name
        self.age = age
        self.skills = skills
        self.style = style

    def get_player(self):
        print(self.name,self.age,self.skills,self.style)


class Team(object):
    def _init_(self, name):
        self.name = name
        self._players = []

    def add_player(self, obj):
        if isinstance(obj, Player):
            self._players.append(obj)
        else:
            print("Please provide player object")

    def get_players(self):
        for player in self._players:
            player.get_player()


if _name_ == "_main_":

    p1 = Player("Mahendra", 46, "Wicket Kipper", "Right-Hand Batsman")
    p2 = Player("Sachin", 35, "Batsman", "Right-Hand Batsman")
    p3 = Player("Saurabh", 44, "Batsman", "Left-Hand Batsman")
    p4 = Player("Zahir", 38, "Bauwller", "Medium Pace Bauwller")
    p5 = Player("Yuvraj", 43, "All rounder")

    t = Team("India")
    t.add_player(p1)
    t.add_player(p2)
    t.add_player(p3)
    t.add_player(p4)
    t.add_player(p5)

    t.get_players()- 👋 Hi I’m @Dhanshiyaprakash902514
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Dhanshiyaprakash902514/Dhanshiyaprakash902514 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

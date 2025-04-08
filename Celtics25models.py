import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# Sample User Model
class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

class Player(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Age = models.IntegerField()
    DraftYear = models.IntegerField()
    DraftPick = models.IntegerField()

    def __str__(self):
        name = str(self.FirstName) + " " + str(self.LastName)
        return name

class Team(models.Model):
    TeamName = models.CharField(max_length=100)

    class Meta:
        ordering = ["TeamName"]

    def __str__(self):
        return str(self.TeamName)

class FormerTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    YearJoined = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        team = "".join([str(team) for team in self.team.TeamName])
        return f"{self.player.FirstName} {self.player.LastName}, {team}, {self.YearJoined}"

class Accolade(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    Championships = models.IntegerField()
    MVPs = models.IntegerField()
    ROTY = models.BooleanField()
    DPOY = models.IntegerField()
    AllStars = models.IntegerField()
    AllNBAs = models.IntegerField()
    
    def __str__(self):
        return str(self.player.FirstName) + " " + str(self.player.LastName) + " Accolades"

class Contract(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    ContractSalary = models.IntegerField()
    ContractYears = models.IntegerField()

    def __str__(self):
        return str(self.player.FirstName) + " " + str(self.player.LastName) + " Contract"

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    Minutes = models.FloatField()
    PPG = models.FloatField()
    APG = models.FloatField()
    RPG = models.FloatField()
    SPG = models.FloatField()
    BPG = models.FloatField()
   
    def __str__(self):
        return str(self.player.FirstName) + " " + str(self.player.LastName) + " Stats" 

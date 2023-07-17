from django.db import models

class Trades(models.Model):
    team1 = models.CharField(max_length=500)
    team2 = models.CharField(max_length=500)
    trade_type = models.TextField(default='Player')
    players_team1  = models.TextField(default="players_team1", null=True)
    players_team2 = models.TextField(default="players_team2", null=True, blank=True)
    compensation = models.TextField(default="0.1", null=True, blank=True)
    description = models.TextField(default="Description")
    title = models.TextField(default="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    net_salary = models.TextField(default="0")

class Players(models.Model):
    name = models.TextField()
    salary = models.DecimalField(decimal_places=2,max_digits=4)
    team = models.TextField()
    role = models.TextField(default="role")
    #nation = models.TextField(default='nation')
    image = models.TextField(default='image')
    nation = models.TextField(default='nation')

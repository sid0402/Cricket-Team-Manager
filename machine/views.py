from django.shortcuts import render
from .models import Trades, Players

players = Players.objects.exclude(team="Unsold")

def team_details(team1, team2):
    team1q = Players.objects.filter(team=team1)
    team2q = Players.objects.filter(team=team2)
    overseas1 = team1q.filter(nation='Overseas')
    overseas2 = team2q.filter(nation='Overseas')
    team1_oplayers = len(overseas1)
    team2_oplayers = len(overseas2)
    team1_salary=0
    team2_salary=0
    for i in range(len(team1q.values_list('salary'))):
        team1_salary+=float(team1q.values_list('salary')[i][0])
    for i in range(len(team2q.values_list('salary'))):
        team2_salary+=float(team2q.values_list('salary')[i][0])
    return team1_oplayers, team2_oplayers, round(team1_salary,2), round(team2_salary,2)

def new_details(request,team1, team2, team1_players, team2_players):
    flag=False
    message = []
    if (len(team1_players) == 0) or (len(team2_players)==0):
        flag=True
        message.append("Trade must have atleast one player or price")
    team1_oplayers,team2_oplayers, team1_salary,team2_salary  = team_details(team1, team2)
    team1_space = round(95 - team1_salary,2)
    team2_space = round(95 - team2_salary,2)
    team1_playerspace = 8 - team1_oplayers
    team2_playerspace = 8 - team2_oplayers
    team1_players_salary = 0
    team2_players_salary = 0
    for i in team1_players:
        salary_one = Players.objects.filter(name=i).values_list('salary')
        team1_players_salary+=salary_one[0][0]
    for i in team2_players:
        salary_two = Players.objects.filter(name=i).values_list('salary')
        team2_players_salary+=salary_two[0][0]
    team1_net_salary = team2_players_salary - team1_players_salary
    team2_net_salary = team1_players_salary - team2_players_salary
    team1_net_players = len(team2_players) - len(team1_players)
    team2_net_players = len(team1_players) - len(team2_players)

    print("NET",team1_net_salary)

    request.session['net_salary'] = str(team1_net_salary)

    print("DNDJNDON",request.session['net_salary'])

    if (team1_net_salary > team1_space) or (team2_net_salary > team2_space):
        flag=True
        message.append("Salaries do not work out. {} has {} Cr left and {} has {} Cr left.".format(team1, team1_space, team2,team2_space))

    return round(team1_net_salary,2), round(team2_net_salary,2), flag, message

def validate_compensation(team1, team2, players_team1, compensation1):
    flag=False
    message = []
    if (len(players_team1) == 0):
        flag=True
        message.append("Trade must have atleast one player or price")
    team1_numplayers,team2_numplayers, team1_salary,team2_salary  = team_details(team1, team2)
    players1_overseas = 0
    team1_players_compensation = 0
    for i in range(len(players_team1)):
        team1_players_compensation+=float(compensation1[i])
        team1q = Players.objects.filter(name=players_team1[i]).filter(nation='Overseas')
        if (len(team1q)):
            players1_overseas+=1
    if (team2_salary+team1_players_compensation > 95):
        flag=True
        message.append("Salaries do not work out. {} has {} Cr left and players would bring in {} Cr.".format(team1, 95-team1_salary, team1_players_compensation))
    if (team2_numplayers+players1_overseas > 8):
        flag=True
        message.append("Number of overseas players do not work out. {} has {} overseas players out of 8.".format(team2, team2_numplayers))
    return team1_players_compensation, flag, message

def trade_submitted(request):
    team1=request.session['team1']
    team2=request.session['team2']
    players_team1=request.session['players_team1']
    players_team2=request.session['players_team2']
    description=request.POST.get('description')
    title = request.POST.get('title')
    trade_type = request.session['trade_type']
    compensation=request.session['compensation1']
    net_salary = str(request.session['net_salary'])
    request.session['flag'] = True

    if (trade_type=='compensation'):
        trade = Trades(team1=team1,team2=team2,
        players_team1=players_team1,
        compensation=compensation,
        description=description, title=title, trade_type='compensation',net_salary=net_salary)
        trade.save()
    else:
        trade = Trades(team1=team1,team2=team2,
        players_team1=players_team1,
        players_team2=players_team2,
        description=description, title=title, trade_type='player',net_salary=net_salary)
        trade.save()
    
    return render(request, 'submitted.html', {'team1':team1, 'team2':team2})

def trade(request):
    print(request.POST)

    team1=request.session['team1']
    team2=request.session['team2']
    trade_type = request.session['trade_type']
    
    players_team1=request.POST.getlist('player_team1')
    players_team2=request.POST.getlist('player_team2')
    request.session['players_team1'] = players_team1
    request.session['players_team2'] = players_team2
    
    players_list=[]
    players_dict=[]
    for j in players_team1:
        players_list.append(j)
    
    if (trade_type=='compensation'):
        compensation1 = request.POST.get('compensation1').split(',')
        request.session['compensation1'] = compensation1

        team1_players_compensation, flag, message = validate_compensation(team1, team2, players_team1, compensation1)

        players=Players.objects.filter(name__in=players_list)

        if (flag):
            message=message[0]
            context = {'team1':team1,'team2':team2,
            'players':players,
            'compensation':team1_players_compensation, "error":message,'type':trade_type}
            return render(request, 'trade-failed.html', context)
        else:
            message="Trade Successful!"
            message=message[0]
            context = {'team1':team1,'team2':team2,
            'players':players,
            'compensation':team1_players_compensation, "error":message,'type':trade_type}
            return render(request, 'trade-successful.html', context)
    else:
        team1_net_salary, team2_net_salary, flag, message = new_details(request, team1, team2, players_team1, players_team2)

        for j in players_team2:
            players_list.append(j)
        players=Players.objects.filter(name__in=players_list)

        if (flag):
            message=message[0]
            context = {'team1':team1,'team2':team2,
            'players':players, "error":message,
            "net1":team1_net_salary, "net2":team2_net_salary, 'type':trade_type}
            return render(request, 'trade-failed.html', context)
        else:
            message="Trade Successful!"
            context = {'team1':team1,'team2':team2,
            'players':players, "error":message,
            "net1":team1_net_salary, "net2":team2_net_salary,'type':trade_type}
            return render(request, 'trade-successful.html', context)

def machine(request):
    team1 = request.POST.get('team1')
    team2 = request.POST.get('team2')
    trade_type = request.POST.get('trade_type')
    
    request.session['team1'] = team1
    request.session['team2'] = team2
    request.session['trade_type'] = trade_type

    team1_players,team2_players, team1_salary,team2_salary  = team_details(team1, team2)

    context = {'players':players,'team1':team1,'team2':team2, 'team1_players':team1_players,
    'team2_players':team2_players,'team1_salary':round(team1_salary,2),'team2_salary':round(team2_salary,2)}
    
    if (trade_type=="player"):
        return render(request,"machine-players.html",context)
    else:
        return render(request,"machine-compensation.html",context)

def home(request):
    return render(request, 'home.html', {"players":players})

def make_players_list(players):
    players = players.replace('[','').replace(']','').replace("\'",'').split(',')
    players = [x.strip() for x in players]
    return players

def make_compensation_list(comp):
    comp = comp.replace('[','').replace(']','').replace("\'",'').split(',')
    comp = [float(x.strip()) for x in comp]
    return comp
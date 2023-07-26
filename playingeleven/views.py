from django.shortcuts import render
from django.http import HttpResponse
from machine.models import Trades, Players


def home(request):
    request.session['flag']=False
    return render(request, 'playingeleven/home.html')


def selector(request):
    chosen_team = request.POST.get('team')
    request.session['chosen_team'] = chosen_team

    flag = request.session['flag']
    
    if (request.POST.get('flag')):
        flag_auction = int(request.POST.get('flag'))
    else:
        flag_auction=0

    request.session['flag_auction'] = flag_auction
    auction_type = request.session['auction_type']

    players_team1 = request.session['players_team1']
    players_team2 = request.session['players_team2']
    trade_type = request.session['trade_type']
    
    players = Players.objects.filter(team=chosen_team)

    if (flag_auction == 2):
        if (auction_type == 'mega'):
            auction_team = request.session['new_team']
            players = Players.objects.filter(name__in=auction_team[0])
            auction_team = request.session['auction_team']
            context = {'players':players,'team1':auction_team}
            return render(request, 'playingeleven/selector.html', context)
        elif (auction_type == 'mini'):
            miniauction_team = request.session['miniauction_team']
            players = Players.objects.filter(name__in=miniauction_team)
            auction_team = request.session['auction_team']
            context = {'players':players,'team1':auction_team}
            return render(request, 'playingeleven/selector.html', context)
    elif (flag==1):
        if (len(players_team1) != 0):
            for p in players_team1:
                players = players.exclude(name=p)
        if (len(players_team2) != 0):
            for p in players_team2:
                players = players.exclude(name=p)

        player1_team=''
        player2_team=''

        for p in Players.objects.filter(name=players_team1[0]):
            player1_team = p.team
        if (trade_type != 'compensation' and len(players_team2)!=0):
            for p in Players.objects.filter(name=players_team2[0]):
                player2_team = p.team

        players_list = []
        for player in players:            
            players_list.append({'name': player.name, 'image': player.image, 'role':player.role})

        if (chosen_team == player1_team):
            for p in players_team2:
                players2 = Players.objects.filter(name=p)
                for p2 in players2:
                    players_list.append({'name': p2.name, 'image': p2.image, 'role':p2.role})
        if (chosen_team == player2_team or trade_type=='compensation'):
            for p in players_team1:
                players1 = Players.objects.filter(name=p)
                for p2 in players1:
                    players_list.append({'name': p2.name, 'image': p2.image, 'role':p2.role})
        context = {'team1': chosen_team, 
            'players': players_list, 'players_team1': players_team1,
               'players_team2': players_team2, 'range': range(1, 12)}
    else:
        context = {'team1': chosen_team, 
            'players': players, 'players_team1': players_team1,
            'players_team2': players_team2, 'range': range(1, 12)}

    return render(request, 'playingeleven/selector.html', context)

def team(request):
    flag_auction = int(request.session['flag_auction'])
    if (flag_auction==2):
        chosen_team = request.session['auction_team']
    else:
        chosen_team=request.session['chosen_team']
    team = request.POST.getlist('playing-eleven')
    row1=team[0:6]
    row2=team[6:11]
    try:
        impact=team[11]
    except:
        impact=""
    row1 = Players.objects.filter(name__in=row1).order_by('role')
    row2 = Players.objects.filter(name__in=row2).order_by('role')
    if (impact != ""):
        impact = Players.objects.filter(name=impact).order_by('role')
    else:
        impact = ""
    context={'row1':row1,'row2':row2,'impact':impact,'chosen_team':chosen_team.upper()}
    return render(request, 'playingeleven/team.html', context)

from django.shortcuts import render
from machine.models import Players

# Create your views here.
def home(request):
    return render(request, 'auction/home.html')

def retain(request):
    auction_team = request.POST.get('team')
    auction_type = request.POST.get('auction_type')
    request.session['auction_team'] = auction_team
    request.session['auction_type'] = auction_type
    players = Players.objects.filter(team = auction_team)
    context = {'team':auction_team, 'auction_type':auction_type,'players':players}
    if (auction_type=='mega'):
        return render(request, 'auction/retain.html', context)
    elif (auction_type=='mini'):
        return render(request, 'auction/retain-mini.html', context)

def simulate(request):
    retained=[]
    if request.POST.get('ret1'):
        retained.append(request.POST.get('ret1'))
    if request.POST.get('ret2'):
        retained.append(request.POST.get('ret2'))
    if request.POST.get('ret3'):
        retained.append(request.POST.get('ret3'))
    if request.POST.get('ret4'):
        retained.append(request.POST.get('ret4'))
    request.session['retained_players'] = retained
    price = [16, 12, 8, 6]
    ret_list = []
    purse = 0
    overseas = 0
    for i in range(len(retained)):
        player = Players.objects.filter(name=retained[i])
        ret_list.append({'name':retained[i],'image':player[0].image,'price':price[i]})
        purse+=price[i]
        if (player[0].nation == 'Overseas'):
            overseas+=1
    request.session['ret_list'] = ret_list
    request.session['retained_purse'] = purse
    allplayers = Players.objects.exclude(name__in=retained)
    context =  {'retained': ret_list,'purse':95-purse,'minplayers':18-len(retained),'maxoverseas':8-overseas,'allplayers':allplayers}
    return render(request, 'auction/simulate.html', context)

def simulatemini(request):
    retained=request.POST.getlist('retained')
    request.session['retained_mini'] = retained
    purse = 0
    overseas = 0
    for i in range(len(retained)):
        player = Players.objects.filter(name=retained[i])
        purse+=player[0].salary
        if (player[0].nation == 'Overseas'):
            overseas+=1
    #request.session['retained_purse'] = purse
    allplayers = Players.objects.exclude(name__in=retained)
    retained_players = Players.objects.filter(name__in=retained)
    context =  {'retained': retained_players,'purse':95-purse,'minplayers':18-len(retained),'maxoverseas':8-overseas,'allplayers':allplayers}
    return render(request, 'auction/simulate-mini.html', context)

def team(request):
    auction_type = request.session['auction_type']
    if (auction_type == 'mega'):
        players_chosen = request.POST.getlist('playerchosen')
        ret_list = request.session['ret_list']
        retained_players = []
        for player in ret_list:
            retained_players.append(player['name'])
        new_team = request.session['retained_players']
        team_name = request.session['auction_team']
        for i in players_chosen:
            new_team.append(i)
        request.session['new_team'] = new_team,
        players = Players.objects.filter(name__in=new_team)
        salary=0
        overseas=0
        for player in players:
            if (player.name in retained_players):
                for ret_player in ret_list:
                    if ret_player['name'] == player.name:
                        ret_salary = ret_player['price']
                player.salary = ret_salary
            salary+=player.salary
            if (player.nation == 'Overseas'):
                overseas+=1
        print(players)
        context = {'players':players, 'team':team_name,'salary':salary,'overseas':overseas, 'numplayers':len(players)}
        return render(request, 'auction/team.html', context)
    elif (auction_type == 'mini'):
        players_chosen = request.POST.getlist('playerchosen')
        team_name = request.session['auction_team']
        retained = request.session['retained_mini']
        auction_team = retained
        salary = 0
        overseas = 0
        for player in players_chosen:
            auction_team.append(player)
            player_obj = Players.objects.filter(name=player)[0]
            salary+= player_obj.salary
            if (player_obj.nation == "Overseas"):
                overseas+=1
        for player in retained:
            player_obj = Players.objects.filter(name=player)[0]
            salary+= player_obj.salary
            if (player_obj.nation == "Overseas"):
                overseas+=1
        request.session['miniauction_team'] = auction_team
        players = Players.objects.filter(name__in=auction_team)
        context = {'players':players, 'team':team_name,'salary':salary,'overseas':overseas, 'numplayers':len(players)}
        return render(request, 'auction/team.html', context)
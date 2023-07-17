from django.shortcuts import render, redirect
from django.http import HttpResponse
from machine.models import Trades, Players
from .forms import CommentsForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

trades = Trades.objects.all().order_by('created_at').reverse()
    
def home(request):
    trades = Trades.objects.all().order_by('created_at').reverse()
    p = Paginator(trades, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'trades':trades, 'page_obj':page_obj}
    return render(request, 'forum/home.html', context)

def post_details(request, pk):
    post = None
    players_list = []
    for i in trades:
        if (i.id == int(pk)):
            post = i
    try:
        players_team1 = make_players_list(post.players_team1)
        print(post.players_team2)
        if (post.players_team2 != 'players_team2'):
            players_team2 = make_players_list(post.players_team2)
        else:
            players_team2=[]
        compensation = make_compensation_list(post.compensation)
        for j in players_team1:
            players_list.append(j)
        for j in players_team2:
            players_list.append(j)

        players_traded = Players.objects.filter(name__in=players_list)

        r = [x for x in range(len(players_team1))]

        team1=post.team1
        team2=post.team2

        teams=[]
        for player in players_traded:
            if not(player.team in teams):
                teams.append(player.team)
        team1 = teams[0]
        if (len(teams)==2):
            team2=teams[1]

        print(float(post.net_salary))
        team1_net = float(post.net_salary)
        team2_net=float(0-team1_net)

        comments = post.comments.all()
        new_comment = None
        # Comment posted
        if request.method == 'POST':
            comment_form = CommentsForm(data=request.POST)
            if comment_form.is_valid():
                # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.trade = post
                # Save the comment to the database
                new_comment.save()
        else:
            comment_form = CommentsForm()

        if (post.trade_type=='compensation'):
            team1_net=sum(compensation)
            team2_net=0-sum(compensation)

        print(compensation)
        context = {'post': post, 'players':players_traded, 'players_team1':players_team1,
        'players_team2':players_team2, 'team1':team1,'team2':team2,
        'net1':team1_net,'net2':team2_net, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form, 'compensation':compensation}

        return render(request, 'forum/post.html', context)
    except:
        messages.error(request, "REFRESH PAGE")
        return redirect(home)

def make_players_list(players):
    players = players.replace('[','').replace(']','').replace("\'",'').split(',')
    players = [x.strip() for x in players]
    return players

def make_compensation_list(comp):
    comp = comp.replace('[','').replace(']','').replace("\'",'').split(',')
    comp = [float(x.strip()) for x in comp]
    return comp
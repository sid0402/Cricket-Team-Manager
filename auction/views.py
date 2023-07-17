from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'auction/home.html')

def retain(request):
    team = request.POST.get('team')
    auction_type = request.POST.get('auction_type')
    request.session['auction_team'] = team
    request.session['auction_type'] = auction_type
    context = {'team':team, 'auction_type':auction_type}
    return render(request, 'auction/retain.html', context)
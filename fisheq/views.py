from django.shortcuts import render, redirect
from .models import day_profit, roomcodes, users

# Create your views here.

def home(request) :
    if request.method == 'POST' :
        username = request.POST['nick']
        rc = request.POST['cd']
        user = users()
        user.name = username
        user.roomcode = rc
        user.save();
        #return redirect('team?p%s' %(rc))
        user = users.objects.all().filter(roomcode=rc)
        tn = len(user)%4
        if tn==0 :
            tn=4
        print(tn)
        return redirect('team',rc, tn)
    else :
        roomcode = roomcodes.objects.all()
        tn = 1
        return render(request, 'index.html', {'roomcode': roomcode})

def team(request, code, tn) :
    if request.method == 'POST' :
        c = request.POST['fish']
        profit = day_profit.objects.all().filter(roomcode=code)
        if len(profit)==0 :
            print("!@#$%^&")
            p = day_profit()
            p.day = 0
            p.roomcode=code
        else :
            p = profit.objects.all().filter(day__lt=4)
            if len(p)==0 :
                p = day_profit()
                p.day = 0
                p.roomcode=code
        p.day = p.day + 1
        p.team1 = 1
        p.team2 = 1
        p.team3 = 1
        p.team4 = 1
        if tn==1 :
            p.team1 = c
        elif tn==2 :
            p.team2 = c
        elif tn==3 :
            p.team3 = c
        else :
            p.team4 = c
        if p.day == 4 :
            if p.team1+p.team2+p.team3+p.team4 == 8 :
                cost = 25
            elif p.team1+p.team2+p.team3+p.team4 == 7 :
                cost = 50
            elif p.team1+p.team2+p.team3+p.team4 == 6 :
                cost = 62.5
            elif p.tea1+p.team2+p.team3+p.team4 == 5 :
                cost = 75
            else :
                cost = 100
            p.team1 = p.team1*cost-75
            p.team2 = p.team2*cost-75
            p.team3 = p.team3*cost-75
            p.team4 = p.team4*cost-75
        p.save();
        return redirect('sell',code)
    else :
        user = users.objects.all().filter(roomcode=code)
        return render(request, 'boat.html', {'user':user, 'tn':tn})

def sell(request,code) :
    profit = day_profit.objects.all().filter(roomcode=code)
    return render(request, 'market.html', {'profit':profit})
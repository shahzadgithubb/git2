from django.shortcuts import render

# Create your views here.
def master(request) :
    return render(request,'dailyacc/master.html')
def condact(request) :
    return render(request,'dailyacc/condact.html')

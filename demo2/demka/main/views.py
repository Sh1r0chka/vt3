from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from main.forms import *

from main.models import Ticket, Status


def index(request):
    return render(request, 'main/index.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add-ticket')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tickets')
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'main/login.html')


def ticket_view(request):
    if request.user.is_superuser:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(creator=request.user).order_by('id')
    print(tickets)
    return render(request, 'main/tickets.html', {'tickets': tickets})


def add_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        form.instance.creator = request.user
        form.instance.status = Status.objects.get(title="Новое заявление")
        if form.is_valid():
            form.save()
            return redirect('tickets')
        else:
            raise Http404
    else:
        form = NewTicketForm()
    return render(request, 'main/add-ticket.html', {'form': form})


def edit_ticket(request, id):
    try:
        ticket = Ticket.objects.get(id=id)
        status = Status.objects.order_by('id')
        if request.method == 'POST':
            new_status_id = request.POST.get("status")
            ticket.status_id = new_status_id
            ticket.save()
            return redirect('tickets')
        else:
            return render(request, "main/edit-ticket.html", {"ticket": ticket, "status": status})
    except Ticket.DoesNotExist:
        return HttpResponseNotFound("<h2>Заявление не найдено</h2>")
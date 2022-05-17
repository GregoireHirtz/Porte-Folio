from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import get_object_or_404, render
from models import models

User = get_user_model()

def index(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    return redirect('accueil')


def accueil(request):
    projet = models.Projet.objects.all()
    return render(request, 'web/accueil.html', context={"projets": projet})


def connexion(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('accueil')
        else:
            return render(request, 'user/connexion.html', context={'erreur': 1})
    else:
            return render(request, 'user/connexion.html', context={'erreur': 0})

def inscription(request):
	if request.user.is_authenticated:
		return redirect('accueil')

	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')
			password2 = request.POST.get('password2')
			user = authenticate(username=username, password=password)
			if user:
				return render(request, 'user/inscription.html', context={'erreur': 2})
			else:
				if password == password2:
					user = User.objects.create_user(username=username, password=password)
					login(request, user)
					return redirect('accueil')	
				else:
					return render(request, 'user/inscription.html', context={'erreur': 1})
		else:	
			return render(request, 'user/inscription.html', context={'erreur': 0})

def deconnexion(request):
    logout(request)
    return redirect('accueil')

def projet_detail(request, slug):
    projet = get_object_or_404(models.Projet, slug=slug)
    return render(request, 'web/detailProjet.html', context={'projets': projet})

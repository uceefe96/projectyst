# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Etudiant, Module
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import redirect
from django.contrib import messages



@login_required
def accueil(request):
    return render(request, 'accueil.html')

@login_required
def selectionner_etudiant(request):
    if request.method == 'POST':
        cne = request.POST['cne']
        cin = request.POST['cin']
        etudiant = get_object_or_404(Etudiant, cne=cne, cin=cin)
        return render(request, 'choisir_attestation.html', {'etudiant': etudiant})
    else:
        return render(request, 'selectionner_etudiant.html')

@login_required
def bilan_de_notes(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    modules = etudiant.modules.all()
    return render(request, 'bilan_de_notes.html', {'etudiant': etudiant, 'modules': modules})

@login_required
def attestation_universitaire(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    return render(request, 'attestation_universitaire.html', {'etudiant': etudiant})

@login_required
def attestation_d_inscription(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    return render(request, 'attestation_d_inscription.html', {'etudiant': etudiant})




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cne = form.cleaned_data['cne']
            cin = form.cleaned_data['cin']
            user = authenticate(request, cne=cne, cin=cin)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'CNE ou CIN incorrect.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



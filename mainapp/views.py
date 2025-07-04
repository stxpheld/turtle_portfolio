from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Photo, Categorie
from .forms import ContactForm
from .forms import PhotoForm


# Create your views here.
def home(request):
    # Récupérer toutes les catégories pour les boutons
    categories = Categorie.objects.all()

    # Vérifier s'il y a un filtre
    categorie_nom = request.GET.get('categorie')
    if categorie_nom:
        photos = Photo.objects.filter(categorie__nom=categorie_nom)
        categorie_active = categorie_nom
    else:
        photos = Photo.objects.all()
        categorie_active = None

    # Gestion du formulaire contact
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            # autres champs si tu veux
            print("Nouveau message reçu de :", nom)
            return render(request, 'contact_success.html', {
                'nom': nom,
                'photos': photos,
                'categories': categories,
                'categorie_active': categorie_active,
            })
    else:
        form = ContactForm()

    return render(request, 'base.html', {
        'form': form,
        'photos': photos,
        'categories': categories,
        'categorie_active': categorie_active,
    })


@login_required
def ajouter_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galerie')  # redirection vers la galerie
    else:
        form = PhotoForm()
    return render(request, 'ajouter_photo.html', {'form': form})
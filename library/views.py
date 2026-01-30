from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Genre, Author, Language
from .forms import GenreForm, AuthorForm, LanguageForm, BookForm

def home(request):
    context = {
        'genres': Genre.objects.all(),
        'authors': Author.objects.all(),
        'languages': Language.objects.all(),
    }
    return render(request, 'home.html', context)


@login_required
def add_genre(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Add Genre'})


@login_required
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Add Author'})


@login_required
def add_language(request):
    form = LanguageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Add Language'})


@login_required
def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Add Book'})


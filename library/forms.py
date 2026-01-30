from django import forms
from .models import Genre, Author, Language, Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'genre', 'language']

from django import forms
from API.books.models import Book
from API.buyers.models import Buyer
from API.genres.models import Genre
from API.authors.models import Authors
from API.publication.models import Publication
from API.assembly.models import BookAssembly
from API.sales.models import Sale
from API.suppliers.models import Supplier


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Book Title'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Synopsis', 'rows': 3}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Authors
        fields='__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author Name'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Biography', 'rows': 3}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre Name'}),
        }


class BookAssemblyForm(forms.ModelForm):
    class Meta:
        model=BookAssembly
        fields='__all__'
        widgets={
            'binding_type': forms.Select(attrs={'class': 'form-control'}),
            'paper_type': forms.Select(attrs={'class': 'form-control'}),
            'cover_type': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight in grams'}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model=Publication
        fields='__all__'
        widgets={
            'book': forms.Select(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'edition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edition'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'page_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Page Count'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Language'}),
            'assembly': forms.Select(attrs={'class': 'form-control'}),
            'price_unit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Unit Price'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields='__all__'
        widgets={
            'person_type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'document': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BuyerForm(forms.ModelForm):
    class Meta:
        model=Buyer
        fields='__all__'
        widgets={
            'person_type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'document': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model=Sale
        fields='__all__'

        widgets={
            'buyer': forms.Select(attrs={'class': 'form-select'}),
            'book': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'})


        }

from django import forms

from french_bulldog_store.helpers.form_control import FormControl
from french_bulldog_store.web.models import AlbumPhoto


class CreatePhotoForm(forms.ModelForm, FormControl):
    class Meta:
        model = AlbumPhoto
        fields = ('name', 'description', 'age', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Enter your dog name",
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter a brief description for your dog'
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': "Enter your dog's age",
                },
            ),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()
        self.user = user

    def save(self, commit=True):
        photo = super().save(commit=False)

        photo.user = self.user

        if commit:
            photo.save()

        return photo

class EditPhotoForm(forms.ModelForm, FormControl):
    class Meta:
        model = AlbumPhoto
        fields = ('name', 'description', 'age', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Edit dog's name",
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Edit description'
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Edit age',
                },
            ),
        }


class DeletePhotoForm(forms.ModelForm):
    class Meta:
        model = AlbumPhoto
        fields = ()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

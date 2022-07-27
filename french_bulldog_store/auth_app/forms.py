from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from french_bulldog_store.auth_app.models import Customer
from french_bulldog_store.helpers.form_control import FormControl
from french_bulldog_store.web.models import AlbumPhoto


class CreateProfileForm(FormControl, auth_forms.UserCreationForm):
    name = forms.CharField(
        max_length=Customer.NAME_MAX_LENGTH,
    )
    picture = forms.ImageField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    def save(self, commit=True):
        user = super().save(commit=commit)

        customer = Customer(
            name=self.cleaned_data['name'],
            picture=self.cleaned_data['picture'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            customer.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'name', 'picture')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name',
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'placeholder': 'Upload picture',
                }
            ),
        }


class EditProfileForm(FormControl, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    class Meta:
        model = Customer
        fields = ('name', 'picture', 'email')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name',
                }
            ),
            'picture': forms.FileInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        user = get_user_model()
        AlbumPhoto.objects.filter(user_id=user.id).delete()
        Customer.objects.filter(id=user.id).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Customer
        fields = ()


from django.urls import path

from french_bulldog_store.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, Profile, \
    EditProfileView, DeleteProfileView, ProductCreateView, ProductEditView, ProductDeleteView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='profile delete'),

    path('add/product/', ProductCreateView.as_view(), name='add product'),
    path('edit/product/<int:pk>/', ProductEditView.as_view(), name='edit product'),
    path('delete/product/<int:pk>/', ProductDeleteView.as_view(), name='delete product'),
)
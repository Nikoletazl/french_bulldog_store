
from django.urls import path

from .views import HomePageView, Store, CreatePhotoView, EditPhotoView, DeletePhotoView
from ..cart.views import updateItem, process_order

urlpatterns = [
    path('', HomePageView.as_view(), name="home page"),

    path('store/', Store.as_view(), name="store"),
    path('update_item/', updateItem, name="update item"),
    path('process_order/', process_order, name="process order"),

    path('create/photo/', CreatePhotoView.as_view(), name="create photo"),
    path('edit/photo/<int:pk>', EditPhotoView.as_view(), name="edit photo"),
    path('delete/photo/<int:pk>', DeletePhotoView.as_view(), name="delete photo"),
]

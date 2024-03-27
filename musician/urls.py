
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='musician'),
    path('edit/<int:id>',views.edit,name="edit_musician")
]

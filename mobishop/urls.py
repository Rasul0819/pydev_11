from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage),
    path('product/<int:id>/',views.detail,name='azamat')
]
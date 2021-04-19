from django.urls import path
from . import views

app_name="diary"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:year>/<int:month>", views.add_month, name="add_month"),
]

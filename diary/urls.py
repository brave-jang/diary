from django.urls import path
from . import views

app_name="diary"

urlpatterns = [
    path("", views.main, name="main"),
    path("<int:year>/<int:month>/", views.Detailcalendar, name="Detailcalendar"),
    path("todo/", views.write_todo, name="todo"),
    path("trans_todo/<int:pk>/", views.trans_todo, name="trans_todo"),
]

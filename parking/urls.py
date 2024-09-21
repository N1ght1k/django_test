from django.urls import path
from . import views

app_name = "parking"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/", views.tag_handler, name="tag_handler"),
    path("current/", views.get_current, name="get_current"),
]

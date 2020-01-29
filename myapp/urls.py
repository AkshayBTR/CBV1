from django.urls import path
from myapp import views

app_name="myapp"
urlpatterns = [
    path('list/',views.SchoolListView.as_view(),name="list"),
]

from django.urls import path
from Gun import views
from Gun.models import Gun

Gun_list_view = views.GunListView.as_view(
    queryset=Gun.objects.all(),
    context_object_name="gun_list",
    template_name="Gun/gunDisplay.html",
)
urlpatterns = [
    path("", views.home, name="home"),
    path("gunDisplay/", Gun_list_view, name="gunDisplay"),
    path("about/", views.about, name="about"),

]
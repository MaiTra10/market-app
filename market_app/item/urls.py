from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "item"

urlpatterns = [
    
    path("add/", views.add, name = "add"),
    path("browse/", views.browse, name = "browse"),
    path("<int:pk>/delete/", views.delete, name = "delete"),
    path("<int:pk>/edit/", views.edit, name = "edit"),
    path("<int:pk>/", views.details, name = "detail")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

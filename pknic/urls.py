from django.urls import path

from pknic import views

urlpatterns = [
    path("lookup/<str:domain>", views.lookup_domain),
]

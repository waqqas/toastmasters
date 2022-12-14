"""toastmasters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "gamification/",
        include(("gamification.urls", "gamification"), namespace="gamification"),
    ),
    path(
        "event/",
        include(("event.urls", "event"), namespace="event"),
    ),
    path("_nested_admin/", include("nested_admin.urls")),
    path(
        "model_api/",
        include(("model_api.urls", "model_api"), namespace="model_api"),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

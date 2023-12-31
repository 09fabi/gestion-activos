"""
URL configuration for gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required
from gestion_app.views import (
    HomePageView,
    CreateActivoView,
    CreateReportView,
    ActivosView,
    LogoutView,
    LoginView,
    ActivoInfoView,
    ReportsView,
    AdminView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login_required(HomePageView.as_view()), name='home'),
    path('create_activo/', login_required(CreateActivoView.as_view()), name='create_activo'),
    path('create_report/', login_required(CreateReportView.as_view()), name='create_report'),
    path('activos/', login_required(ActivosView.as_view()), name='activos'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activo_info/', login_required(ActivoInfoView.as_view()), name='activo_info'),
    path('reports/', login_required(ReportsView.as_view()), name='reports'),
    path('admin/', login_required(AdminView.as_view()), name='admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

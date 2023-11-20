from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Activo, Report, CustomUser
from .forms import ActivoForm, ReportForm
from django.views import View
from django.contrib.auth import authenticate, login

class HomePageView(View):
    template_name = 'gestion_app/homepage.html'

    def get(self, request):
        if request.user.is_authenticated:
            username = request.user.nombre
            message = f"Bienvenido {username}!"
        else:
            message = "Bienvenido!"

        context = {'message': message}

        return render(request, self.template_name, context)
    
class CreateActivoView(View):
    template_name = 'gestion_app/create_activo.html'

    def get(self, request):
        form = ActivoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activos')
        else:
            return render(request, self.template_name, {'form': form})
 
class CreateReportView(View):
    template_name = 'gestion_app/create_report.html'

    def get(self, request):
        form = ReportForm()
        activos = Activo.objects.all()
        selected_activo = 'YourActivotTitulo'
        return render(request, self.template_name, {'form': form, 'activos': activos, 'selected_activo': selected_activo})

    def post(self, request):
        form = ReportForm(request.POST)
        activos = Activo.objects.all()
        selected_activo = 'YourActivotTitulo'

        if form.is_valid():
            form.save()
            return redirect('reports')
        
        return render(request, self.template_name, {'form': form, 'activos': activos, 'selected_activo': selected_activo})
    
class ActivosView(View):
    def get(self, request):
        activos = Activo.objects.all()
        return render(request, 'gestion_app/activos.html', {'activos': activos})

class ReportsView(View):
    def get(self, request):
        reports = Report.objects.all()
        return render(request, 'gestion_app/Reports.html', {'reports': reports})
    
class LogoutView(View):
    def get(self, request):
        return render(request, 'gestion_app/login.html')
  
class LoginView(View):
    template_name = 'gestion_app/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        correo = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(correo=correo)

        if user.password == password:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
            return render(request, self.template_name)
        
class ActivoInfoView(View):
    def get(self, request):
        return render(request, 'gestion_app/detalle.activo.html')

class AdminView(View):
    def get(self, request):
        return render(request, 'gestion_app/admin.html')

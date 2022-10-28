from django.shortcuts import render

# Create your views here.
from .forms import PerfilForm
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario
from django.urls import reverse_lazy


@method_decorator(login_required, name="dispatch")
class PerfilUpdate(UpdateView):
    form_class = PerfilForm
    success_url = reverse_lazy("profile")
    template_name = "registration/perfil_form"

    def get_object(self):
        perfil, creado = PerfilUsuario.objects.get_or_create(usuario=self.request.user)
        return perfil

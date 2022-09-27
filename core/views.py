from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/index.html"
    dicc_context = {"titulo": "Clase de Django Avanzado", "profesor": "Eder Lara T."}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.dicc_context)

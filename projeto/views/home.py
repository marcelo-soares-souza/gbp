from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "base/home.html"

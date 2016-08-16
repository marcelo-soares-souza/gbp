from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "base/home.html"


class Permission(TemplateView):
    template_name = "base/permission.html"


class About(TemplateView):
    template_name = "base/content/about.html"


class Location(TemplateView):
    template_name = "base/content/location.html"

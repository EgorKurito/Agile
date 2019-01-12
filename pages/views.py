from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPAgeView(TemplateView):
    template_name = 'pages/about.html'

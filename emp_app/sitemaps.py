from django.contrib.sitemaps import Sitemap
from .models import Employee 
from django.urls import reverse

class EmpSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Employee.objects.all()

class StaticViewSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.9
    def items(self):
        return ['view_emp','add_emp','filter_emp']

    def location(self, item):
        return reverse(item)
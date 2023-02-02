from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.

class HomeView(View):
    template_name = 'index.html'
    storequery = Store.objects.all()

    def get_storequery(self):
        return self.storequery

    def get(self, request):
        context = {
            'stores': self.get_storequery(),
        }

        return render(request, self.template_name, context)

class MerchantView(View):
    template_name = 'merchant.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
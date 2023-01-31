from django.shortcuts import render
from django.views import View


# Create your views here.

def HomeView(request):
    tmeplate = 'index.html'
    context = {}

    return render(request, tmeplate, context)

class MerchantView(View):
    template_name = 'merchant.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
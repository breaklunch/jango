
from django.views import View
from .models import Company

class CompanyView(View):
    
    def get(self,request):
        companies=Company.objects.all()

    def post(self,request):
        pass
    
    def put(self,request):
        pass
    
    def delete(self,request):
        pass
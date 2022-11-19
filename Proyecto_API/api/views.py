
from django.http import JsonResponse
from django.views import View
from .models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company=companies[0]
                datos = {'message' :"Completado", 'companies' : companies}
            else:
              datos = {'message':"Companias no encontradas"}
            return JsonResponse(datos)
        else:    
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {'message' :"Completado", 'companies' : companies}
            else:
                datos = {'message':"Companias no encontradas"}
            return JsonResponse(datos)

    def post(self,request):
       #print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
       datos = {'message':"Completado"}
       return JsonResponse(datos)
    
    def put(self,request):
        jd = json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company=Company.objects.get(id=id)
            Company.name=jd['name']
            Company.website=jd['website']
            Company.foundation=jd['foundation']
            Company.save()
            datos = {'message':"Succes"}
        else:
            datos = {'message':"Companias no encontradas"}   
        return JsonResponse(datos)
    
    def delete(self,request):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {'message':"Completado"}
        else: 
            datos = {'message': "Compania no encontrada"}
        return JsonResponse(datos)
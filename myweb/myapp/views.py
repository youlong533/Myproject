from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Case
# Create your views here.
def index(request):
    #return HttpResponse("Hello world!")
    return render(request, "index.html")

def case(request):
    #获取所有stu表信息
    lists = Case.objects.all()
    print(lists)
    #获取单条学生信息
    print(Case.objects.get(id=1))

    return HttpResponse("ok")
#from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import aish
# Create your views here.
def aishwarya(request):

    if request.method == 'POST':

        a1 = request.POST.get("name")

        a2 = request.POST.get("address")

        a3 = request.POST.get("empId")

        a4 = request.POST.get("staffid")

        a = aish(name=a2,address=a2,empId=a3,staffid=a4)

        a.save()

        print(a1)

        print(a2)

        print(a3)

        print(a4)

    else:

        return render(request,"page1.html",context={})

    return HttpResponse("printed on Console, please Check!!")
  
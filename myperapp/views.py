from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
import time
# Create your views here.


def home(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    cont=request.POST.get('text')
    cont +=f"\nemail of person is : {email}\n"
    send_mail(name,cont,'badhrinadh.g.v.s@gmail.com',['narayanacollage265@gmail.com'], fail_silently=False)
    messages.success(request,'Messages send successfully,will contact you soon!!')
    return redirect('/')
  else:
    return render(request,'real.html')
    

def projects(request):
  return render(request,'projects.html')

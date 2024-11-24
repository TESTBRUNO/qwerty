from django.shortcuts import render, redirect
from myapp.models import product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.



def card(request,cardid):
  data = product.objects.filter(id = cardid)
  return render(request,"card.html", {"data":data})


def reg(request):
  if request.method == "POST":
    data = request.POST
    new = User.objects.create_user(data["lgn"],data["email"],data["psw"])
    new.save()
  return render(request,"reg.html")




def auth (request):
  if request.method == "POST":
    data = request.POST
    user = authenticate(username = data["lgn"], password =  data["psw"])
    if user is not None:
      request.session["is_auth"] = user.id
      return redirect(index)
      
    else:
      return redirect(auth)

  else:
    return render(request,"auth.html")




def index(request):
  
  if request.session.get("is_auth",False):
    user = User.objects.filter(id = request.session.get("is_auth",False))
    
    if request.method == "POST":
      data = request.POST
      print(data)
      print(data["name"])

      new = product(name = data["name"],description = data["desc"], cost = data ["cost"], count = data["count"])
      new.save()


    res = product.objects.all()
    return render(request,"index.html", {"test":res, "user":user})
  
  else:
    return HttpResponse("Не авторизован")



def main(request):
  data = product.objects.all()
  return render(request, "main.html", {"test":data})







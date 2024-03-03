import email
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
#def index(request):
    #return render(request,'index.html')
def loandre(request):
    if request.method == "POST":
        if request.POST.get('submit') =="register":
            username = request.POST.get('username')
            email    = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = models.User.objects.filter(username=username).first()
            if user_obj:
                return HttpResponse("用户已存在")
            else :
                user_obj = models.User(username=username,email=email,password=password)
                user_obj.save()  # 保存数据 
                return  HttpResponse("成功")       
        elif request.POST.get('submit') == "login":        
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = models.User.objects.filter(email=email).first()
            if user_obj:
                if password == user_obj.password:
                    return redirect('https://blog.csdn.net/m0_62186690?type=blog')
                else:
                    return HttpResponse("密码错误")
            else:
                return HttpResponse("用户不存在")
    
    return render(request,'loandre.html')   
        
# Create your views here.

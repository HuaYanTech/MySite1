from django.shortcuts import HttpResponse,render,redirect
from app01 import models
from django.views import View
def lzr(request):
    return render(request, 'xxx/hellolzr.html')
    #return HttpResponse('Hello Lzr')

def index(request):
    return HttpResponse('你好，我爱你')

def login(request):
    errormsg=''
    if request.method=='POST':
        email = request.POST.get('email', None)
        pwd = request.POST.get('pwd', None)
        if email == '1220264596@qq.com' and pwd == '12345678':
            return redirect('http://www.jd.com')
        else:
            errormsg='账号或者密码错误'
    return render(request,'login.html',{"error":errormsg})

def baobao(request):
    email=request.POST.get('email',None)
    pwd=request.POST.get('pwd',None)
    if email=='1220264596@qq.com' and pwd=='12345678':
        return HttpResponse('OK')
    else:
        return HttpResponse('Not Ok')

def userlist(request):
    ret = models.UserInfo.objects.all()
    looms = models.Looms.objects.all()
    if request.method=='GET':
        id=request.GET.get('id',None)
    if not id:
        id=looms[0].Id
        #print(ret)
    else:
        id=int(id)
    return render(request, 'userlist1.html', {'userlist':ret,'looms':looms,'activeId':id})

class Userlist(View):
    def __init__(self):
        self.ret = models.UserInfo.objects.all()
        self.looms = models.Looms.objects.all()
    def get(self,request):
        id = request.GET.get('id', None)
        if not id:
            id = self.looms[0].Id
        else:
            id = int(id)
        return render(request, 'userlist1.html', {'userlist': self.ret, 'looms': self.looms, 'activeId': id})

def adduser(request):
    if request.method=='POST':
        newname=request.POST.get('username',None)
        models.UserInfo.objects.create(name=newname)
        return redirect('/userlist/')
    return render(request, 'adduser.html')

def deluser(request):
    del_id=request.GET.get('id',None)
    if del_id:
        delobj=models.UserInfo.objects.get(id=del_id)
        delobj.delete()
        return redirect('/userlist/')

def edituser(request):
    if request.method=='POST':
        edit_id=request.POST.get('userid')
        new_name=request.POST.get('username')
        editobj=models.UserInfo.objects.get(id=edit_id)
        editobj.name=new_name
        editobj.save()
        return redirect('/userlist/')
    userid=request.GET.get('id')
    if userid:
        editobj=models.UserInfo.objects.get(id=userid)
        return render(request,'edituser.html',{'edituser':editobj})

def test1(request):
    # data=[f'第{i:0>3}号技师' for i in range(1,11)]
    return render(request, 'test.html')


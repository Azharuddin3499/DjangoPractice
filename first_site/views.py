from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm
from service.models import Service
from news.models import News
def homePage(request):
    data={
        "title": 'Home Page',
        'data':'Azhar Welcome',
        'clist':['JAVA','Python','C#','C'],
        'clints':[
            {'name':'Azhar','Ph':'03412324556'},
            {'name':'Kareem','Ph':'03112346536'},
            {'name':'Kareem2','Ph':'03112346536'},
            {'name':'Kareem3','Ph':'03112346536'}
        ]
    }
    return render(request,"index.html",data)

def contact(request):
    serviceData = Service.objects.all().order_by('-service_title')
    data ={
        'serviceData':serviceData
    }
    return render(request,'contact.html',data)


def newsdetails(request,newsid):
    newsDetails=News.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,'contact.html',data)


def submitform(request):
    data={}
    ans=0
    try:
        if request.method=="POST":
            n1=int(request.POST['n1'])
            n2=int(request.POST['n2'])
            ans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':ans
            }
            return HttpResponse(ans)
    except:
        pass


def newsapp(request):
    newsData =News.objects.all()
    data={
        'newsData':newsData
    }
    return render(request,'newsapp.html',data)


def service(request):
    if request.method=="GET":
        output=request.GET['output']
    return render(request,'services.html',{'output':output})

def userForm(request):
    #GET method
    # ans=0
    # try:
    #     n1=int(request.GET['n1'])
    #     n2=int(request.GET['n2'])
    #     ans=n1+n2
    # except:
    #     pass

    #POST METHOD
    data={}
    ans=0
    try:
        if request.method=="POST":
            n1=int(request.POST['n1'])
            n2=int(request.POST['n2'])
            ans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':ans
            }
            url="/services/?output={}".format(ans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass
    return render(request,'userForm.html',data)




def courseDetails(request,id):
    return HttpResponse(id)


def calculator(request):
    c=''
    try:
        n1=eval(request.POST['num1'])
        n2=eval(request.POST['num2'])
        opr=request.POST['opr']
        if opr=='+':
            c=n1+n2
        elif opr=='-':
            c=n1-n2
        elif opr=='*':
            c=n1*n2
        elif opr=='/':
            c=n1/n2
    except:
        c='Invalid Input'
    print(c)
    return render(request,'calculator.html',{'data':c})
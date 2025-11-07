from django.shortcuts import render
from .models import *
# Create your views here.


# class dq(models.Model):
#     seasion = models.ForeignKey(seasions, on_delete=models.CASCADE ,related_name='deslr', default=1)
#     subject = models.ForeignKey(titels , on_delete=models.CASCADE ,related_name='day_question')
#     body = models.TextField()
#     answer = models.IntegerField()
#     why=models.TextField()


# def main(request):
#     s=seasions.objects.get(seasions=1)
#     a=titels.objects.filter(seasion=s)

#     # question.objects.create(subject=a, body='''یتانتانیبتانابنتانابنتانب
#     #                         بتاتنیابنتانیتانتاینلانایناالبنانیانیبانانبانبیالنباتل
#     #                         یبلانلانیانلتایتنلاینیانتبنتانتانتیالنانانتالنتتیبانگگگ''')
#     for t in a:
#         dq.objects.create(seasion=s ,subject=t, body='''   سوال اول دو دو تا چند تاست''',choice1='1',
#                           choice2='2',choice3='4',choice4='3',answer = 3 , why='''برای اینکه زیرا ''')
#     # titels.objects.create(seasion=s, subjects='قوانین دمورگان')
#     # titels.objects.create(seasion=s, subjects='مجموعه')
#     # titels.objects.create(seasion=s, subjects='مجموعه')

#     return render(request,'index.html')


def main(request):
    s= seasions.objects.all()
    print(str(s).split())
    return render(request,'index.html',{'s':s})
def subject(request,id):
    s=seasions.objects.get(seasions=id)
    a=titels.objects.filter(seasion=s)
    return render(request,'second_page.html',{'a':a ,'id':str(id)})
def title(request , t , a):
    print([list(str(a))])
    print([str(t)])
    return render(request,'Third.html' , {'t':[str(t)],'a':[str(a)]})
def information(request, t,a):
    # print(type(a))
    # for i in a:
    #     print(i)
    # print(o)
    o=int(a[2])
    s=seasions.objects.get(seasions=o)
    q=titels.objects.get(seasion=s , subjects=t)
    print(q)
    b=question.objects.filter(seasion=s ,subject=q)
    # print(b)
    return render(request,'description.html',{'b':b,'s':s,'t':t})
def questions(request,t,s):
    print(t,s)
    s=int(s[2])
    # s=seasions.objects.get(seasions=o)
    q=titels.objects.get(seasion=s , subjects=t)
    print(q)
    b=question.objects.filter(seasion=s ,subject=q)
    for i in b:
        # for t in i:
            # for k in t:
        print('''
              
              
              
              
              ''',i.choice1)
    return render(request,'six.html',{'b':b})
def daq(request,t,s):
    s=int(s[2])
    # s=seasions.objects.get(seasions=o)
    q=titels.objects.get(seasion=s , subjects=t)
    print(q)
    b=dq.objects.filter(seasion=s ,subject=q)
    for i in b:
        print(t)
    return render(request,'six.html',{'b':b})
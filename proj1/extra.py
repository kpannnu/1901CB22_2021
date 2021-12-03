# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     d={'name':'Abhijeet','place':'Mars'}
#     return render(request,'index.html',d)
    # return HttpResponse('''<h2>Abhijeet is learning</h2> <a href="https://stud.iitp.ac.in/?loginOp=logout"> IITP Zimbra website</a>''')
# def about(request):
#     return HttpResponse('About the learning process')
# # def index(request): 
# #     file = open("mysite/check.txt",'r+')
# #     return HttpResponse(file.read())
# from django.http import HttpResponse
# def index(request):
#     nav = '''<div style="padding:50px;height:100vh;width:100%;background:lightblue;">
#                 <h1 style="padding-bottom:20px;"> Hello Abhijeet Singh </h1>
               
#                 <div style="display:flex;">
#                     <a href="/removepunc" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">Removepunc</a> 
                       
#                     <a href="/capfirst" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">Capfirst</a>
#                     <a href="/spaceremover" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">SpaceRomover</a>
#                 </div>
                
#                  <h3 style="padding:20px 0;">Page content in the below</h3>
#             </div>
#         '''
#     return HttpResponse(nav)
# def removepunc(request):
#     return HttpResponse('<h1>Remove Punctuations</h1><br><br><br>'
#                         '<a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">Back to Home page</a>')
# def capitalizefirst(request):
#     return HttpResponse('<h1>Capitalize First</h1><br><br><br>'
#                         '<a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">Back to Home page</a>')
# def spaceremover(request):
#     return HttpResponse('<h1>Space Remover</h1><br><br><br>'
#                         '<a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;border-radius:10px;color:white;">Back to Home page</a>')


# urls.py lines
# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index,name='index'),
#     path('about', views.about,name='about'),
#     # path('', views.index,name='index'),
# ]
# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index, name="index"),
    # path('removepunc',views.removepunc, name="removepunc"),
    # path('capfirst',views.capitalizefirst, name="capitalizefirst"),
    # path('spaceremover',views.spaceremover, name="spaceremover")
# ]
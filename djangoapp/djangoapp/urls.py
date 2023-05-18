from django.urls import path
from myapp import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('back/',views.back_view,name='back'),
    path('form', views.classify_image, name='classify_image'),
    path('classify', views.classify_captured_image, name='classify'),
]

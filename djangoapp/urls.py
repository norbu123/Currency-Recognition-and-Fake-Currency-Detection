from django.urls import path
from myapp import views 
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('back/',views.back_view,name='back'),
    path('form', views.classify_image, name='classify_image'),
    path('classify', views.classify_captured_image, name='classify'),
    
    if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

]


from django.contrib import admin
from django.urls import path
from projeto_web import views
from django.views.generic import RedirectView
from  django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
# mas aqui e o primerio que voce tende fazer
#depois que voce criar aqui voce vai la para a views.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresa/all/',views.list_all_empresa),
    path('empresa/user/',views.list_user_empresa),
    path('empresa/detail/<id>/',views.empresa_detail),
    path('login/',views.login_user),
    path('login/submit',views.submit_login),
    path('logout/',views.logout_user),
    path('empresa/register/',views.register_empresa),
    path('empresa/register/submit',views.set_empresa),
    path('empresa/delete/<id>/',views.delete_empresa),
    path('',RedirectView.as_view(url='empresa/all/'))

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
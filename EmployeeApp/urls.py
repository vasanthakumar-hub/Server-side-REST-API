from django.urls import path, include
from . import views
#from .DjangoAPI.urls import urlpatterns

urlpatterns = [
    path('department',views.departmentApi),
    path('department/<int:id>',views.departmentApi) # to accepting ID as integer on API calls/request

]
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inservice_form,name='inservice_insert'), # get and post req. for insert operation
    path('<int:id>/', views.inservice_form,name='inservice_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.inservice_delete,name='inservice_delete'),
    path('list/',views.inservice_list,name='inservice_list'),
    
]

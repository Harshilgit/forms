from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.master_form,name='master_insert'), # get and post req. for insert operation
    path('<int:id>/', views.master_form,name='master_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.master_delete,name='master_delete'),
    path('list/',views.master_list,name='master_list') # get req. to retrieve and display all records
]
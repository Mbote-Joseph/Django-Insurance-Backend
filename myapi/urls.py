
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('get', views.getCustomer, name='get'),
    path('post', views.postCustomer, name='post'),
    path('put/<int:pk>', views.putCustomer, name='put'),
    path('delete/<int:pk>', views.deleteCustomer, name='delete'),
]
from django.urls import path
from . import views

app_name  = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('system-users/', views.systemUsers, name='systemUsers'),
    path('manage-items/', views.manageProducts, name='manageProducts'),
    path('request-item/', views.requestItem, name='requestItem'),
    path('requests/', views.stockRequests, name='stockRequests'),
    path('requests/<int:pk>/approve/', views.stockRequestsApprove, name='stockRequestsApprove'),
    path('requests/<int:pk>/return/', views.stockReturn, name='stockReturn'),
]

from django.urls import path

from user_center import views


urlpatterns = [
    # 用户管理
    path('', views.UserViewset.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('<int:pk>', views.UserViewset.as_view({
        'patch': 'partial_update',
        'get': 'retrieve',
    })),
]

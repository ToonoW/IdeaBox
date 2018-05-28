from django.urls import path

from ideas import views


urlpatterns = [
    # 想法
    path('', views.IdeaViewset.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('<int:pk>', views.IdeaViewset.as_view({
        'patch': 'partial_update',
        'get': 'retrieve',
    })),
]

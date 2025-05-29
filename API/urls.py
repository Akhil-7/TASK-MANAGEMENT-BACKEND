from django.urls import path, include

urlpatterns = [
    path('account/', include('userManage.urls')),
    path('task/', include('taskManage.urls')),
]

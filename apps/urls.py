from django.urls import path

from apps.views import CategoryCreateListApiView, ProductCreateListApiView

urlpatterns = [
    path('category', CategoryCreateListApiView.as_view()),
    path('product', ProductCreateListApiView.as_view())
]
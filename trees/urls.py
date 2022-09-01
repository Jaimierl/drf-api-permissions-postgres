from django.urls import path
from .views import TreeList, TreeDetail

urlpatterns = [
    path('', TreeList.as_view(), name='tree_list'),
    path('<int:pk>', TreeDetail.as_view(), name='tree_detail')
]

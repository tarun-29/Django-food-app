from django.contrib import admin
from django.urls import path
# from . import views
from .views import FoodDetail, index, item, detail, create_item, update_item, delete_item, IndexClassView, CreateItem

app_name = 'food'
urlpatterns = [
    # path('', index, name='index'),
    path('', IndexClassView.as_view(), name='index'),
    # path('<int:item_id>/', detail, name='detail'),
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),
    path('item/', item, name='item'),
    # path('add', create_item, name='create_item'),
    path('add', CreateItem.as_view(), name='create_item'),

    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', delete_item, name='delete_item')
]

from django.urls import path

from webapp import views
from webapp.views import ReviewView, ReviewUpdate, ReviewDelete

urlpatterns = [
    # Product urls
    path('', views.ProductIndexView.as_view(), name='index'),
    path('product/<int:pk>/detail', views.ProductDetail.as_view(), name='product_detail'),
    path('product/add', views.CreateProduct.as_view(), name='product_add'),
    path('product/<int:pk>/update', views.UpdateProduct.as_view(), name='product_update'),
    path('product/<int:pk>/delete', views.DeleteProduct.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', views.DeleteProduct.as_view(), name='confirm_delete'),
    # Review urls
    path('review/<int:pk>/review/', ReviewView.as_view(), name='review'),
    path('review/<int:pk>/review/update', ReviewUpdate.as_view(), name='review_update'),
    path('review/<int:pk>/review/delete', ReviewDelete.as_view(), name='review_delete'),
    path('review/<int:pk>/confirm_review_delete/', views.ReviewDelete.as_view(), name='confirm_review_delete'),
]
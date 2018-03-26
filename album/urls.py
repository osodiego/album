from django.urls import path
from album import views

urlpatterns = [

    path( '', views.base, name='base' ),

    path( 'category/', views.CategoryListView.as_view(), name='category-list' ),

    path( 'category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category-detail' ),

    path( 'photo', views.PhotoListView.as_view(), name='photo-list' ),

    path( 'photo/<int:pk>/detail', views.PhotoDetailView.as_view(), name='photo-detail' ),

    path( 'photo/<int:pk>/create', views.PhotoCreate.as_view(), name='photo-create' ),

    path( 'photo/<int:pk>/update', views.PhotoUpdate.as_view(), name='photo-update' ),

    path( 'photo/<int:pk>/delete', views.PhotoDelete.as_view(), name='photo-delete' ),
]

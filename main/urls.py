from django.urls import path

from main.views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('<int:category_id>/', category_view, name='category'),

    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('create_category/', create_category_view, name='create_category'),
    path('update/<int:id>/', update_category_view, name='update_category'),
    path('delete/<int:id>/', delete_category_check_view, name='delete_category_check'),
    path('delete_cat/<int:id>/', delete_category_view, name='delete_cat'),

    path('upload_photo/<int:category_id>/', upload_photo_view, name='upload_photo'),
    path('update_photo/<int:id>/<int:category_id>/', update_photo_view, name='update_photo'),
    path('delete_photo/<int:id>/<int:category_id>/', delete_photo_view, name='delete_photo'),

]

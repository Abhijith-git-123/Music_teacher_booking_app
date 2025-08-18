"""music_teacher_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from music_teacher_booking_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home',views.admin_home),
    path('login_post',views.login_post),
    path('',views.login_get),
    path('logout',views.logout),
    path('add_category_get',views.add_category_get),
    path('add_category_post',views.add_category_post),
    path('view_category_admin',views.view_category_admin),
    path('edit_category_get/<id>',views.edit_category_get),
    path('edit_category_post/<id>',views.edit_category_post),
    path('delete_category/<id>',views.delete_category),
    path('view_musicteacher_verifie',views.view_musicteacher_verifie),
    path('accept_teacher/<id>',views.accept_teacher),
    path('reject_teacher/<id>',views.reject_teacher),
    path('view_verified_teacher',views.view_verified_teacher),
    path('view_rating_admin',views.view_rating_admin),
    path('view_user',views.view_user),
    path('view_feedback',views.view_feedback),
    path('change_password_get',views.change_password_get),
    path('change_password_post',views.change_password_post),


####################music_teacher##########################################


    path('musicteacher_home',views.musicteacher_home),
    path('musicteacher_register_get',views.musicteacher_register_get),
    path('musicteacher_register_post',views.musicteacher_register_post),
    path('view_category',views.view_category),
    path('add_own_category_get/<id>',views.add_own_category_get),
    path('add_own_category_post/<id>',views.add_own_category_post),
    path('view_own_category',views.view_own_category),
    path('edit_own_category_get/<id>',views.edit_own_category_get),
    path('edit_own_category_post/<id>',views.edit_own_category_post),
    path('delete_own_category/<id>',views.delete_own_category),
    path('add_class_time_get/<id>',views.add_class_time_get),
    path('add_class_time_post/<id>',views.add_class_time_post),
    path('view_timesloats',views.view_timesloats),
    path('edit_time_sloat_get/<id>',views.edit_time_sloat_get),
    path('edi_time_sloat_post/<id>',views.edi_time_sloat_post),
    path('view_request',views.view_request),
    path('accept_request/<id>',views.accept_request),
    path('rejet_requestt/<id>',views.rejet_request),
    path('request_allote_time',views.request_allote_time),
    path('view_alote_time/<id>/<rid>',views.view_alote_time),
    path('allocate_times/<id>/<rid>',views.allocate_times),
    path('view_payment_history',views.view_payment_history),
    path('view_rating',views.view_rating),
    path('view_verified_request',views.view_verified_request),
    path('delete_time_slot/<id>',views.delete_time_slot),


############################################USER#################################################

    path('user_index',views.user_index),
    path('user_register',views.user_register),
    path('user_register_post',views.user_register_post),
    path('view_all_category',views.view_all_category),
    # path('view_all_category_post',views.view_all_category_post),
    path('view_teacher_from_category/<id>',views.view_teacher_from_category),
    path('send_request/<id>',views.send_request),

    path('user_view_rating/<id>',views.user_view_rating),
    path('view_user_request',views.view_user_request),
    path('view_approved_request',views.view_approved_request),
    path('view_rejected_request',views.view_rejected_request),
    path('make_payment',views.make_payment),
    path('send_rating_get/<id>',views.send_rating_get),
    path('send_rating_post/<id>',views.send_rating_post),
    path('send_feedback_get',views.send_feedback_get),
    path('send_feedback_post',views.send_feedback_post),
    path('user_payment/<id>/<fee>',views.user_payment),
    path('payment_complete/<id>',views.payment_complete),








]

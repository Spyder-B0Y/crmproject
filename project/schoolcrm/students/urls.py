from django.urls import path
from . import views

urlpatterns = [

    path("", views.school_login),   

    path("login/", views.school_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("students/", views.students, name="students"),
    path("add-student/", views.add_student, name="add_student"),
    path("delete-student/<int:id>/", views.delete_student, name="delete_student"),
    path("edit-student/<int:id>/", views.edit_student, name="edit_student"),
    path("logout/", views.logout_view, name="logout"),

]
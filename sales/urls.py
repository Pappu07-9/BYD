from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.saleshome,name="saleshome"),
    path('add', views.adddata, name="adddata"),
    path('insert', views.insert, name='inserts'),
    path('edit/<int:id>', views.editdata, name='editdata'),
    path('delete/<int:id>', views.deletedata),
    path('update_edit/<int:id>', views.update_edit, name='updateedit'),
]
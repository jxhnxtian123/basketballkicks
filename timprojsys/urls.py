from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),   
    path('products/',views.products, name="products"),
    path('records/',views.records, name="records"),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('update/<int:id>', views.update, name='update'),
    path('cancel1/<int:id>', views.cancel1, name='cancel1'),
    path('update1/<int:id>', views.update1, name='update1'),
]

from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='homeurl'),
    path('login/',views.user_login,name='loginurl'),
    path('signup/',views.user_signup,name='signupurl'),
    path('logout/',views.user_logout,name='logouturl'),
    path('mycart/',views.mycart,name='mycarturl'),
    path('myorders/',views.myorders,name='myorderurl'),
    path('add/<product_id>/',views.add_to_cart, name='add_to_cart'),
    path('add_to_order/<int:item_id>/',views.add_to_order, name='add_to_order'),
    path('remove/<int:item_id>/',views.remove_from_cart, name='remove_from_cart'),
]
    
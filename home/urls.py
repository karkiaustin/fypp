from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', Blog.as_view(), name='blog'),
    path('about/', About.as_view(), name='about'),
    path('bulkbidding/', BulkBidding.as_view(), name='bulkbidding'),
    path('checkout/', CheckOutVehicle.as_view(), name='checkout'),
    path('contact/', stafff, name='contact'),
    path('my_account/', My_Account.as_view(), name='my_account'),
    path('vehicle/', Vehicle.as_view(), name='vehicle'),
    path('signup/', signup, name='signup'),
    path('login/', Login, name='login'),
    path('category/<slug>/', CategoryView.as_view(), name='categoryView'),
    path('type/<slug>/', TypeView.as_view(), name='TypeView'),
    path('detail/<slug>/', VehicleView.as_view(), name='VehicleView'),
    path('search/', SearchView.as_view(), name='search'),
    path('account/logout/', custom_logout, name='logout'),
    path('vehicle_review/<slug>/', vehicle_review, name='review'),
    path('adminhome/', BiddingComment.as_view(), name="AdminHome"),
    path('bidconfirm/<int:id>/', bidconfirm, name="bidconfirm"),
    path('adminbooking/', booking.as_view(), name="adminbooking"),
    path('addvehicle/', AddVehicle, name="AddVehicle"),
    path('updatepw/', updatepaswword, name="password"),
    path('updateprofile/', updateprofile, name="profile"),
    path('startcheckout/<str:id>/', StartCheckout.as_view(), name= "StartCheckout"),
    path('complete/<str:id>/', booking_complete, name="booking_complete"),


]

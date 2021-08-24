from django.urls import path

from . import views

urlpatterns = [
    path('profile-list/', views.ProfileList.as_view(), name='profile-list'),
    # path('list-member/', views.listmemberfamily, name='list-member'),
    # path('vaksin/form/', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    path('profile/<int:pk>', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    path('profile/<int:pk>', views.ProfileDelete.as_view(), name='profile-delete'),
    # path('create/', views.create, name="create"),
    # path('list/', views.list, name="list"),
]

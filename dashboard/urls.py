from django.urls import path
from .views import HomepageView, DashboardView,SearchListingView, ListDetailView
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('', HomepageView.as_view(), name='homepage'),
    path('dashboard', login_required(DashboardView.as_view()), name='dashboard'),
    path('search-listings',SearchListingView.as_view(), name='search-list'),
    path('<int:pk>', ListDetailView.as_view(),name='list-detail'),
    # path('<str:location>', ListDetailView.as_view(), name='list-location')
]
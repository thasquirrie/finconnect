from django.urls import path
from .views import InstitutionView, PlanView, CheckBoxView, AddSuccessView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
 path('add-institution', InstitutionView.as_view(), name='add_institution'),
 path('add-plan', PlanView.as_view(), name='add_plan'),
 path('add-success', AddSuccessView.as_view(), name='add_success'),
 path('checkbox', csrf_exempt(CheckBoxView.as_view()), name='check_box'),
]
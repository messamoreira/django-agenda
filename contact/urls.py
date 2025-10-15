from django.urls import path
from contact.views import contact_views

app_name = 'contact'

urlpatterns = [
    path('', contact_views.index, name='index'),
    path('<int:contact_id>/', contact_views.contact, name='contact'),
]
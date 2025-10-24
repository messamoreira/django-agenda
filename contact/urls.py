from django.urls import path
from contact.views import contact_views, contact_forms

app_name = 'contact'

urlpatterns = [
    path('', contact_views.index, name='index'),
    path('contact/create/', contact_forms.create, name='create'),
    path('<int:contact_id>/', contact_views.contact, name='contact'),
]
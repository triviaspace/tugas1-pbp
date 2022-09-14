# TODO: Implement Routings Here
from django.urls import path
from katalog.views import katalog_view

# TODO: Implement Routings Here
app_name = 'katalog'

urlpatterns = [
    path('', katalog_view, name='katalog_view'),
]

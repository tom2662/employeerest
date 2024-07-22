from django.urls import path
from restemployee.views import *

urlpatterns = [
    path('', view_dtl, name='dtl'),
    path('person/',view_person, name='person'),
]
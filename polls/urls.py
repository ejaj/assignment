from django.urls import path
from polls.views import (
    PollsView,


)
urlpatterns = [
    path('', PollsView.as_view(), name="polls")
]

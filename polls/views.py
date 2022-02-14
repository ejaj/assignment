from django.views import View
from datetime import datetime
from django.http.response import HttpResponse


class PollsView(View):
    def get(self, *args, **kwargs):
        today = datetime.now().today().date()
        return HttpResponse(today)
from hr_part import NewHRQuery

from django.views import generic
from django.http.response import HttpResponse

import json, requests, random, re

PAGE_ACCESS_TOKEN = ''
VERIFY_TOKEN = ''

class NewNLPevent():

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    def post(self, request, *args, **kwargs):
        pass

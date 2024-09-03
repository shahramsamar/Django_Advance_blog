from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def post_list(request):
    return Response("ok api ")
@api_view()
def post_detail(request,id):
    return Response(id)
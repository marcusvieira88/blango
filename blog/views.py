import logging
from django.shortcuts import render

def index(request):
  logger = logging.getLogger(__name__)
  logger.error("log request")
  return render(request, "blog/index.html")

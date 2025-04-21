from django.shortcuts import render, get_object_or_404,redirect 
from django.utils import timezone
from blog.models import Post
import logging
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

logger = logging.getLogger(__name__)

# Create your views here.
@cache_page(300)
@vary_on_cookie
def index(request):
    from django.http import HttpResponse
    logger.debug("Index function is called!")
    return HttpResponse(str(request.user).encode("ascii"))
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})

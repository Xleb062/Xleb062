from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Articles

posts = [

]

def boobs(request):
    return HttpResponse("Hello, World!")


def home(request):
    posts = Articles.objects.order_by("-article_date")[:4]
    # html = ""
    # for post in posts:
    #     html += f"""
    #         <div>
    #             <a HREF="">
    #                 <h1>{post["id"]} - {post["title"]}</h1>
    #             </a>
    #             <p>{post["content"]}</p>
    #         <div/>
    #         """

    return render(request, "posts/home.html", {"posts": posts})


def post(request, id):
    posts = get_object_or_404(Articles, pk=id)
    return render(request, "post/post.html", {"post_dict": post})




#C:\Users\User\PycharmProjects\pythonProject9\mysite\posts\templates



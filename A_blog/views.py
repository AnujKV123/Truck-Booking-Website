from django.shortcuts import render, HttpResponse
from A_blog.models import blog_content
from math import ceil

# Create your views here.


def A_blogHome(request):
    # products = blog_content.objects.all()
    allProds=[]
    catprods= blog_content.objects.values('blog_type', 'sno')
    cats= {item["blog_type"] for item in catprods}
    for cat in cats:
        prod=blog_content.objects.filter(blog_type=cat)
        n = len(prod)
        allProds.append([prod, range(1, n), n])

    params={'allProds':allProds }
    return render(request,"A_blog/index.html",params)

def blogPost(request,slug):
    post=blog_content.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request,"A_blog/blogPost.html",context)

def Search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=blog_content.objects.none()
    else:
        allPostsTitle= blog_content.objects.filter(title__icontains=query)
        allPostsContent =blog_content.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent)
    params={'allPosts': allPosts, 'query': query}
    return render(request,"A_blog/search.html",params)

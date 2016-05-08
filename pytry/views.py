from django.shortcuts import render,Http404,HttpResponse,HttpResponseRedirect,redirect
from .models import Comment
from .forms import PostCommentForm, CommentForm
import json
# Create your views here.


def init_comment_form(request):
    form = PostCommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.left=1
        instance.right=2
        instance.save()
        return HttpResponseRedirect('/pytry/detail/')
    context = {
        "form": form,
    }
    return render(request, "init_comments.html", context)


def comment_form(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        right = form.cleaned_data['right']
        for i in Comment.objects.all().order_by("-right"):

            if i.right >= right:
                i.right += 2

            if i.left > right:
                i.left += 2
            i.save()
        instance = form.save(commit=False)
        instance.left = int(right)
        instance.right = int(right)+1
        instance.save()
        for i in Comment.objects.all().order_by('-right'):
            print i.right
    context={
        "form": form,
    }
    return render(request, "comments_form.html", context)


def comment_detail(request):
    queryset_list = Comment.objects.all().order_by('-left')
    context = {}
    for i in queryset_list:
        context[i.left]=[i.comments, i.right]
        print context.items()
    jsonDumpsIndentStr = json.dumps(context)
    print "jsonDumpsIndentStr=",jsonDumpsIndentStr
    return HttpResponse(jsonDumpsIndentStr)


# def comment_response(request, right):
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.left=right
#         instance.right=right+1
#         instance.save()
#         for i in Comment.objects.all().order_by("-right"):
#             if i.right >= instance.left:
#                 i.right += 2
#             elif i.left>instance.left:
#                 i.left += 2
#             i.save()
#         return HttpResponseRedirect(instance.get_init_absolute_url())
#     queryset_list = Comment.objects.all().order_by("-left")
#     context={}
#     for i in queryset_list:
#         context[str(i.left)]=i.comments
#     jsonDumpsIndentStr = json.dumps(context, indent=1)
#     print "jsonDumpsIndentStr=",jsonDumpsIndentStr
#     return HttpResponse(jsonDumpsIndentStr, "comments_form.html")


# def init_comment(request):
#     form = PostCommentForm(request.POST or None)
#     context = {
#         "comment_list":queryset_list.comments,
#     }
#     return render(request, "comments.html", context)

#
# def init_comment_response(request):
#     queryset_list = Comment.objects.all().order_by("-left")
#     context={}
#     for i in queryset_list:
#         context[str(i.left)]=i.comments
#     jsonDumpsIndentStr = json.dumps(context, indent=1)
#     print "jsonDumpsIndentStr=",jsonDumpsIndentStr
#     return HttpResponse(jsonDumpsIndentStr, "init_comments.html")







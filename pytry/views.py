from django.shortcuts import render,Http404,HttpResponse,HttpResponseRedirect,redirect,get_object_or_404
from .models import Comment
from .forms import PostCommentForm, CommentForm
from django.utils.html import escape
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
    check=False
    errors=[]
    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.comments = escape(instance.comments)
        right = form.cleaned_data['right']
        for i in Comment.objects.all():
            if i.right == right:
                check = True
                break
        if check:
            for i in Comment.objects.all().order_by("-right"):
                if i.right >= right:
                    i.right += 2
                if i.left > right:
                    i.left += 2
                i.save()
            instance.left = int(right)
            instance.right = int(right)+1
            instance.save()
            return HttpResponseRedirect('/pytry/detail/')
        else:
            errors.append("Enter the correct right value")
    context = {
        "form": form,
        "errors": errors,
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


def delete_comment(request):
    check=False
    right=request.POST.get("right")
    left=request.POST.get("left")
    total = int(right)-int(left)+1
    for i in Comment.objects.all():
            if i.right == int(right):
                if i.left == int(left):
                    check = True
                    break
    if check:
        for i in Comment.objects.all().order_by("-right"):
            if i.right <= int(right) and i.left >= int(left):
                i.delete()
            else:
                if i.right >= int(right):
                    i.right -= total
                if i.left > int(right):
                    i.left -= total
                i.save()
    return HttpResponse("success")

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







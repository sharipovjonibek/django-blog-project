from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.views.generic import ListView,View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class home(ListView):
    template_name="blog/home.html"
    model=Post
    ordering=["-date"]
    context_object_name="posts"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data

# def home(request):
#     latest_posts=Post.objects.order_by("-date")[:3]
#     return render(request,"blog/home.html",{
#         "posts":latest_posts,
#     })
    
class all_posts(ListView):
    model=Post
    template_name="blog/all-posts.html"
    ordering=["-date"]
    context_object_name="posts"
    

# def all_posts(request):
#     posts=Post.objects.all().order_by("-date")
#     return render(request,"blog/all-posts.html",
#                   {
#                      "posts":posts, 
#                   })





class post_detail(View):
    def need_later_button(self,request,post):
        if request.session.get("stored_posts"):
            if post.id in request.session.get("stored_posts"):
                need_later_button=False
            else:
                need_later_button=True
        else:
            need_later_button=True
        
        return need_later_button
    
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        form=CommentForm
        return render(request,"blog/post_detail.html",{
            "post":post,
            "tags":post.tags.all(),
            "comment_form":form,
            "comments":post.comments.all().order_by("-id"),
            "need_later_button":self.need_later_button(request,post),
        })

    def post(self,request,slug):
        post=Post.objects.get(slug=slug)
        form=CommentForm(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.post=post
            data.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        
        return render(request,"blog/post_detail.html",{
            "post":post,
            "tags":post.tags.all(),
            "comment_form":form,
            "comments":post.comments.all().order_by("-id"),
            "need_later_button":self.need_later_button(request,post),
        })




    # template_name="blog/post_detail.html"
    # model=Post
    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context["tags"]=self.object.tags.all()
    #     # uploaded_obj=context['post'].tags.all()
    #     # context["tags"]=uploaded_obj
    #     context['comment_form']=CommentForm
    #     return context

# def post_detail(request,slug):
#     # post=Post.objects.get(slug=slug)
#     post=get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post_detail.html",{
#         "tags":post.tags.all(),
#         "post":post,
#     })
# read_later=[]
class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get("stored_posts")
        context={}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"]=[]
            context["has_posts"]=False
        else:
            post=Post.objects.filter(id__in=stored_posts)
            context["posts"]=post
            context["has_posts"]=True
        
        return render(request,"blog/stored-posts.html",context)

        # list_of_id=request.session['stored_posts']
        # list_of_obj=[Post.objects.get(id=id) for id in list_of_id]
        # return render(request,"blog/stored-posts.html",{
        #     "posts":list_of_obj
        # })

    def post(self,request):
        stored_posts=request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts=[]
        
        post_id=int(request.POST['read-later'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
        request.session['stored_posts']=stored_posts
        print(request.session['stored_posts'])
        return HttpResponseRedirect("/")



        # post_id=request.POST['read-later']
        # read_later.append(post_id)
        # request.session['read-later']=read_later
        # print(request.session['read-later'])
        # return HttpResponseRedirect(reverse("post-detail-page",args=[Post.objects.get(id=post_id).slug]))
    


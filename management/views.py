from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from mysite.models import Post, Comment


def home(request):
    return render(request, 'management/home.html')


class PostsView(ListView):
    model = Post
    template_name = 'management/posts.html'
    ordering = ['-published_date']


# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'management/article_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'management/add_post.html'
    fields = ['title', 'image', 'sumText', 'text', 'promote']
    success_url = ''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPostView, self).form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'management/edit_post.html'
    fields = ['title', 'image', 'sumText', 'text', 'promote']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'management/delete_post.html'
    success_url = reverse_lazy('posts')


class CommentsView(ListView):
    model = Comment

    template_name = 'management/comments.html'
    ordering = ['-time']


# class CommentDetailView(DetailView):
#     model = Comment
#     template_name = 'management/comment_detail.html'


class AddCommentView(CreateView):
    model = Comment
    template_name = 'management/add_comment.html'
    fields = '__all__'
    success_url = ''


class UpdateCommentView(UpdateView):
    model = Comment
    template_name = 'management/edit_comment.html'
    fields = '__all__'


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'management/delete_comment.html'
    success_url = reverse_lazy('comments')

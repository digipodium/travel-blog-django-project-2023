from django.shortcuts import render
from .forms import ArticleForm
from .models import *

def article_form(request):
    return render(
        request, 
        'blog/add_blog.html',
        context ={
            'form': ArticleForm(), 
            'title':'Add Content'
    })

def process_article(request):
    ctx = {}
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            ctx['status'] = "Article added successfully"
            form.save()
        else:
            ctx['status'] = "Invalid entries, please fill correctly"
    ctx['form'] = ArticleForm() # create a new form
    return render(request, 'partials/article_form.html', ctx)
    
def process_category(request):
    ctx = {}
    if request.method == 'POST':
        name = request.POST.get('category')
        if len(name) <= 2:
            ctx['status'] = "Category name too short"
        else:
            Category.objects.create(name=name)
            ctx['status'] = "Category added successfully"
    ctx['categories'] = Category.objects.all()
    return render(request, 'partials/category.html', ctx)



def process_tag(request):
    pass

def article_list(request):
    pass

def tag_list(request):
    pass

def category_list(request):
    pass
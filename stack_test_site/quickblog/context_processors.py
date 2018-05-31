from .forms import PostForm

def category_form(request):
    form = PostForm()
    return {'category_form': form}


from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import  Tag
from .forms import TagForm

def affers_page(request):
    tags = Tag.objects.all()
    return render(request, 'affer/affers_page.html', {'tags':tags})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'affer/tags_list.html', context={'tags':tags})



def tags_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'affer/tags_detail.html', context={'tag':tag})


#class TagDetail( View):
    #def get(self, request, slug):
        #tag = Tag.objects.get(slug__iexact=slug2)
        #tag = get_object_or_404(Tag, slug__iexact=slug)
        #return render(request, 'affer/tags_detail.html', context={'tag':tag})




class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'affer/tags_create.html', context={'form':form})

    def post(self, request):
        bound_form = TagForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('akimov:home')
        return render(request, 'affer/tags_create.html', context={'form':bound_form})
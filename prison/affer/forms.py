from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title  = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)
    thumb = forms.ImageField()


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug'],
            thumb=self.cleaned_data['thumb']

        )
        return new_tag
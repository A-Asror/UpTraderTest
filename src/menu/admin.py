from django.contrib import admin
from django.utils.text import slugify
from django.http.request import HttpRequest
from django.forms import Form, ModelForm, ValidationError
from django.contrib import messages
from django.http import HttpResponseRedirect

from src.base.orm import exists_model_from_data

from .models import MenuModel


class MyModelAdminForm(ModelForm):
    class Meta:
        model = MenuModel
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if (title := cleaned_data.get('title', None)) and (cleaned_data.get('slug', None) is not None):
            if (title is not None) and exists_model_from_data(MenuModel, slug=slugify(title), raise_exception=False):
                raise ValidationError(message='Error: The title must be unique')
        return cleaned_data


@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    form = MyModelAdminForm

    # def save_model(self, request: HttpRequest, obj: MenuModel, form: Form, change: bool):
    #     slug = slugify(obj.slug)
    #     if exists_model_from_data(MenuModel, slug=slug, raise_exception=False):
    #         messages.error(request, "Error: The title must be unique")
    #         return HttpResponseRedirect(request.path_info)
    #     else:
    #         super(MenuAdmin, self).save_model(request, obj, form, change)

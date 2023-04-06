from django.shortcuts import render
from django.views.generic import TemplateView

from src.base.orm import base_sql_request

from .models import MenuModel


class MenuPageView(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super(MenuPageView, self).get_context_data(**kwargs)
        context["items"] = MenuModel.objects.all().only("slug")
        return context


def get_template(request, slug: str):
    return render(request, "menu.html", {"items": base_sql_request(MenuModel, only=("slug",))})


# class CustomMenuPageView(TemplateView):
#     template_name = "menu.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(CustomMenuPageView, self).get_context_data(**kwargs)
#         context["items"] = base_sql_request(MenuModel)

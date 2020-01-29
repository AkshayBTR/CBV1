from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView,ListView
from django.views.generic import FormView
from myapp import forms
from myapp.models import *
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'myapp/base.html')

class SchoolListView(ListView):
    model=School
    context_object_name="schools"
    template_name='myapp/school_list.html'
# def index(request):
#     if request.method=="POST":
#         form=forms.DemoForm(request.POST)
#         if form.is_valid():
#             return HttpResponse(str(form.cleaned_data))
#     form=forms.DemoForm()
#     return render(request,'sample.html',context={'form':form})

# class IndexView(View):
#     def get(self,request):
#         form=forms.DemoForm()
#         return render(request,'sample.html',context={'form':form})
    
#     def post(self,request):
#         form=forms.DemoForm(request.POST)
#         if form.is_valid():
#             return HttpResponse(str(form.cleaned_data))

# class DemoTemplateView(TemplateView):
#     template_name="sample.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = forms.DemoForm()
#         return context
    
#     def post(self,request):
#         form=forms.DemoForm(request.POST)
#         if form.is_valid():
#             return HttpResponse(str(form.cleaned_data))
# def sample(request):
#     return HttpResponse("submitted successfully")

# class DemoFormView(FormView):
#     template_name="sample.html"
#     form_class=forms.DemoForm

#     def form_valid(self, form):
#         data=form.cleaned_data
#         print(data)
#         return HttpResponse(str(data))



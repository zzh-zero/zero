from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import StudentForm
from .models import Student
class IndexView(View):
    template_name='index.html'

    def get_context(self):
        students = Student.get_all()
        context={
            'students':students,
        }
        return context
    def get(self,request):
        context =self.get_context()
        form =StudentForm()
        context.update({
            'form':form
        })
        return render(request,self.template_name,context=context)
    def post(self,request):
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form':form
        })
        return render(request, self.template_name, context=context)

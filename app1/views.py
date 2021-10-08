
from app1.forms import SignUpForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from.models import User


# Create your views here.
class UserSignUp(View): 
    def get(self, request):
        form=SignUpForm()
        return render(request,'signup.html', {'forms':form})
    def post(self, request):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Please login Now")
        return redirect('/')

def profileView(request):
    if request.user.is_authenticated:
        user_data=User.objects.all()
    else:
        return redirect("/")
    return render(request, 'detail.html', {'data':user_data})

class Update_View(UpdateView):
    model=User
    form_class=SignUpForm
    template_name='update.html'
    success_url ="/profile/"

class DeleteData(DeleteView):
    model=User
    template_name='user_confirm_delete.html'
    success_url="/profile/"

  


from django.contrib.auth import login,authenticate, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View
from .forms import UserSignUpForm,InstitutionSignUpForm, UserAuthenticateForm
from .decorators import user_required
import json
import re
from django.http import JsonResponse

User = get_user_model()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b'

# Create your views here.
class SignUpView(View):
    def get(self, request):
        template_name = 'authentication/signup.html'
        return render(request, template_name )

#handle username validation
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not (re.fullmatch(regex, email)):
            return JsonResponse({'email_error':'Email is not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry email is in use, choose another one.'}, status=409)
        return JsonResponse({'email_valid':True})

# class UserSignUpView(CreateView):
#     model = User
#     form_class = UserSignUpForm
#     template_name = 'authentication/signupform.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('homepage')



# class InstitutionSignUpView(CreateView):
#     model = User
#     form_class = InstitutionSignUpForm
#     template_name = 'authentication/signupform.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'institution'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('dashboard')


# class LoginUser(CreateView):
#     form_class = UserAuthenticateForm
#     template_name = 'authentication/login.html'
#     # redirect_field_name = 'homepage'
#     def get_success_url(self):
#         """Here is the part where you can implement your login logic """

#         return super().get_success_url()
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                # if user.is_active:
                login(request, user)
                return redirect('homepage')
            print('invalid credentials')
            return render(request, 'authentication/login.html')
        print('fill all fields')   
        return render(request, 'authentication/login.html')
        
            

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/signup.html')
    
    def post(self, request):
        # get user data
        # validate
        # create a user account
        # keep the values in the fiels whrn validation is wrong

        email = request.POST['email']
        password = request.POST['password']
        context = {
            'fieldValues': request.POST
        }
        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                return render(request, 'authentication/signup.html', context )

            user = User.objects.create_user(email=email, password=password)
            user.set_password(password)
            user.save()
            #retirun succes mesage

        return render(request, 'authentication/signup.html')


class LogoutView(View):

    def post(self, request):
        logout(request)
        ##send a logout message
        return redirect('login')

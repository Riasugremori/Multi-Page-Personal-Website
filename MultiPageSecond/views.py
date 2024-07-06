from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
   return render(request, 'greetings.html')

def contact_view(request):
   if request.method == 'POST':
      return redirect('greetings')
   return render(request, 'contact.html')

def greetings_view(request):
   return render(request, 'greetings.html')


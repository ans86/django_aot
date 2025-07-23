from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(name=name, email=email, message=message)

        return render(request, 'thanks.html')  # Show thank you page

    return render(request, 'contact.html')  # Show form again if not POST

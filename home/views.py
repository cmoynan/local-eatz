from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def home(request):
    """
    View for the home page
    """
    return render(request, 'home/index.html')



from django.shortcuts import render

# Create your views here.


def home_page_view(request):

    return render(request, "main/index.html")


def contact_page_view(request):

    return render(request, "main/contact.html")


def portfolio_page_view(request):

    return render(request, "main/portfolio-details.html")



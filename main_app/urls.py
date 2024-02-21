from django.urls import path
from .views import home_page_view, contact_page_view, portfolio_page_view


urlpatterns=[
    path('', home_page_view, name="home"),
    path('contact/', contact_page_view, name="contact"),
    path('portfolio/', portfolio_page_view, name="portfolio")
]
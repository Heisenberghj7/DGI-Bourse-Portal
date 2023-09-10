from django.urls import path, include
from .views import CompanyListView, CompanyDetailView,ManagementListView,ManagementDetailView,ShareholderDetailView,ShareholderListView,ContactDetailView,ContactListView,KeyFigureslView,KeyFiguresListView,RatioslView,RatiosListView,DividendlView,DividendListView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('management/', ManagementListView.as_view(), name='Management-list'),
    path('management/<pk>/', ManagementDetailView.as_view(), name='Management-detail'),
    path('shareholder/', ShareholderListView.as_view(), name='Shareholder-list'),
    path('shareholder/<pk>/', ShareholderDetailView.as_view(), name='Shareholder-detail'),
    path('contact/', ContactListView.as_view(), name='contact-list'),
    path('contact/<pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('keyfigure/', KeyFiguresListView.as_view(), name='keyfigure-list'),
    path('keyfigure/<pk>/', KeyFigureslView.as_view(), name='keyfigure-detail'),
    path('ratios/', RatiosListView.as_view(), name='ratios-list'),
    path('ratios/<pk>/', RatioslView.as_view(), name='ratios-detail'),
    path('dividend/', DividendListView.as_view(), name='Dividend-list'),
    path('dividend/<pk>/', DividendlView.as_view(), name='Dividend-detail'),
]
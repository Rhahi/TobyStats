from django.urls import path

from . import views

app_name = 'tobystats'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('data/', views.ChartView.as_view(), name='getdata'),
    path('data/<mode>/<int:days>/<tz>', views.ChartView.as_view())
]
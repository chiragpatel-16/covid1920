


from django.urls import path
from.import views
from django.contrib.auth.models import User, auth

urlpatterns=[ path('',views.index, name='index'),
              path('reg', views.reg, name='regi' ),
              path('log',views.log, name='log'),
              path('logout',views.logout,name='logout'),
              path('covidinfo', views.covid, name='covidinfo'),
  ]

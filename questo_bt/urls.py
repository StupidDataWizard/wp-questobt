"""project_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'questo_bt'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_quest', views.add_quest, name='add_quest'),
    path('delete_quest/<int:quest_id>', views.delete_quest, name='delete_quest'),
    path('update_status/<int:quest_id>', views.update_status, name='update_status'),
    path('update_priority/<int:quest_id>', views.update_priority, name='update_priority'),
    path('<int:quest_id>/', views.detail, name='detail'),
    path('filter_quests/', views.filter_quests, name='filter_quests'),
    path('solved_quests/', views.solved_quests, name='solved_quests'),
]

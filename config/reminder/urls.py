from django.urls import path
from .views import *

urlpatterns = [
    path('', Reminder_Home.as_view(), name="reminder_home"),
    path('reminder/list/', Reminder_List.as_view(), name="reminder_list"),
    path('reminder/create/', Reminder_Create.as_view(), name="reminder_create"),
    path('reminder/<int:id>/mark/', Reminder_Mark.as_view(), name="reminder_mark"),
]
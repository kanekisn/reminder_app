from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Reminders
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
import pytz

class Reminder_Home(View):
    def get(self, request):
        return render(request, 'reminder/home.html')

class Reminder_List(LoginRequiredMixin, View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        rems = None

        if search_query:
            rems = Reminders.objects.filter(Q(title__icontains=search_query)
                                            | Q(description__icontains=search_query)
                                            & Q(author=request.user))
        else:
            rems = Reminders.objects.filter(author=request.user)
            
        paginator = Paginator(rems, 4)
        page_number = request.GET.get('page', 1)
        page = Paginator.get_page(paginator, page_number)

        context={
            'reminders' : page,
        }
        
        return render(request, 'reminder/reminder_list.html', context)

class Reminder_Create(LoginRequiredMixin, View):
    def get(self, request):
        form = RemindersForm()
        return render(request, 'reminder/reminder_create.html', {'form': form})
    
    def post(self, request):
        form = RemindersForm(request.POST)
        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return render(request, 'reminder/reminder_create.html', {'created_obj' : True, 'form' : RemindersForm()})
        return render(request, 'reminder/reminder_create.html', {'form' : form})

class Reminder_Mark(LoginRequiredMixin, View):
    def get(self, request, id):
        obj = get_object_or_404(Reminders, id__iexact=id)
        
        return render(request, 'reminder/reminder_mark.html', {'obj' : obj})
    
    def post(self, request, id):
        obj = get_object_or_404(Reminders, id__iexact=id)
        obj.is_sent = True
        obj.is_marked = True
        obj.date_com = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        obj.save()
        
        return render(request, 'reminder/reminder_mark_check.html', {'obj' : obj})
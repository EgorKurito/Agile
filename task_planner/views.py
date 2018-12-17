from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Task, Category


class IndexView(generic.ListView):
    template_name = 'task_planner/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Task.objects
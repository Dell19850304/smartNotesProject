from typing import Any, List
from django.db.models.query import QuerySet
from django.shortcuts import render

#My imports
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import DeleteView
from django.http import Http404
from .forms import NotesForm
from .models import Notes

# Create your views here
    

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
    

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url()) 

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url='/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()
        
#def list(request):
#        notes = Notes.objects.all()
#        return render(request,'notes/notes_list.html',{'notes' : notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

#def detail(request,pk):
#    try:
#       note = Notes.objects.get(pk=pk)
#    except Notes.DoesNotExist:
#        raise Http404("The page you looking for is no-where to be found")
#    return render(request,'notes/note_detail.html',{'note':note})
    
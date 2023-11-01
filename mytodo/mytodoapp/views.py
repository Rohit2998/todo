from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        # import ipdb;ipdb.set_trace()
        """Return all the latest todos."""
        print('asdsdasd')
        # return Todo.objects.order_by('-created_at')
    # for api
        kl=list(Todo.objects.all().values().order_by('-created_at')) 
        print('2222222222222')
        return kl
        return JsonResponse(data=kl,status=200)
    def get(self, request):
        # import ipdb;ipdb.set_trace()
        user = self.get_queryset()
        return JsonResponse(data =user,status =200,safe = False)

@require_http_methods(["POST"])
def add(request):
    import ipdb;ipdb.set_trace()
    try:
        title = request.POST['title']
        Todo.objects.create(title=title)
    except:
        print('title not found')
    # return redirect('todos:index')
    return JsonResponse(data ={'status': 'object created'},status =200,safe = False)

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')
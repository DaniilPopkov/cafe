from django.shortcuts import render
from django.views import generic
from .models import Menu
from .forms import MenuForm

class MenuListView(generic.ListView):
    queryset = Menu.objects.all()
    template_name = 'cafe_site/menulist.html'
    context_object_name = 'menu'

class MenuDetailView(generic.DeleteView):
    model = Menu
    template_name = 'cafe_site/menudetail.html'
    context_object_name = 'menu'

class MenuCreate(generic.CreateView):
    form_class = MenuForm
    template_name = 'cafe_site/menucreate.html'

class MenuUpdate(generic.UpdateView):
    model = Menu
    form_class = MenuForm
    template_name='cafe_site/menuupdate.html'
    context_object_name = 'menu'

class MenuDelete(generic.DeleteView):
    model= Menu
    context_object_name ='menu'
    template_name='cafe_site/menu_confirm_delete.html'
    success_url='/'
    
    

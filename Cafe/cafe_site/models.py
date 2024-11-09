from django.db import models
from django.urls import reverse

class Menu(models.Model):
    title=models.CharField(verbose_name='Название', max_length=20)
    text = models.TextField(verbose_name='Описание блюда', null=True, blank=True)
    portion=models.CharField(verbose_name='Порция',max_length=10,blank=True)
    price=models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'
        ordering=['price']


    def get_detailUrl(self):
        return reverse('menu_detail', kwargs={'pk':self.pk})
    
    def get_absolute_url(self):
        return reverse('menu_list')
    
    def get_UpdateUrl(self):
        return reverse('menu_update', kwargs={'pk':self.pk})
    
    def get_DeleteUrl(self):
        return reverse('menu_delete', kwargs={'pk':self.pk})

class Photo(models.Model):
    title=models.CharField(verbose_name='Описание', max_length=30,blank=True, null=True)
    image=models.ImageField(verbose_name='Фотография', upload_to='gallery/')
    menu=models.ForeignKey(Menu, verbose_name='Объявление',on_delete=models.CASCADE)
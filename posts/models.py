from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')
    slug = models.SlugField(unique=True, help_text="Bu joyni qo'lda o'zgartirmaslik tavsiya etiladi.")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Yorliq nomi')
    slug = models.SlugField(unique=True, help_text="Bu joyni qo'lda o'zgartirmaslik tavsiya etiladi.")

    def __str__(self):
        return self.name


class HitCount(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Yorliqlar')
    views = models.ManyToManyField(HitCount, related_name='post_views', blank=True)
    title = models.CharField(max_length=75, verbose_name='Sarlavha')
    slug = models.SlugField(unique=True, help_text='Bu joyni qo`lda o`zgartirmaslik tavsiya etiladi.')
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', verbose_name='Rasm')
    content = RichTextField(verbose_name='Tarkib')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')
    available = models.BooleanField(default=True, verbose_name='Faol passiv')

    def __str__(self):
        return self.title

    def getHitCount(self):
        return self.views.count()

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='Izohlar', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Izoh')
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True, verbose_name='Faol/Passif')

    class Meta:
        ordering = ['-created']  ## Post yorumlarını yeniden eskiye sıralar

    def __str__(self):
        return self.author.username+' | '+ self.post.title
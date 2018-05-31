from django.db import models

# Categorys of Post Model
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(max_length=10000, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

#Post Model
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, null=True)




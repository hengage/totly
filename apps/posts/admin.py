from django.contrib import admin
from .models import Post,  Comment, Category

class CommentInline(admin.StackedInline):
    model = Comment
    extra= 0
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']
    inlines = [ CommentInline ]

class PostInline(admin.StackedInline):
    model = Post
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category_name', 'id', 'slug']
    inlines = [  PostInline ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'commentator']



# admin.site.register(Post, PostAdmin) 
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Comment)
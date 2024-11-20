from django.contrib import admin
from users.models import Post



class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','pub_date']

admin.site.register(Post,PostModelAdmin)
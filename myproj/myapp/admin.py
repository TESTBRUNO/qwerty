from django.contrib import admin
from myapp.models import product



class newprod(admin.ModelAdmin):
  list_display = ["name","description","cost","count","dod"]

admin.site.register(product,newprod)



# Register your models here.
# res = product(name = "")
# res.save()
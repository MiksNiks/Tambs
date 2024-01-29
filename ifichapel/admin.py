from django.contrib import admin
from .models import Baptism, Funerals, Marriage, Blessing, Contact,SchedStatus, paying

admin.site.register(Baptism)
admin.site.register(Funerals)
admin.site.register(Marriage)
admin.site.register(Blessing)
admin.site.register(Contact)
admin.site.register(SchedStatus)
admin.site.register(paying)



from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name="Home"),
    path ('home/', views.home_page, name="Home"),
    path('marriage/', views.marriage_page, name="Marriage"),
    path('about/', views.about_page, name="About"),
    path('birth/', views.birth_page, name="Birth Certificate"),
    path('contact/', views.contact_page, name="Contact Us"),
    path('bless/', views.bless_page, name="Blessing"),
    path('death/', views.death_page, name="Funeral"),
    path('statuspage/', views.status_page, name="Status"),
    path('update/<int:pk>/', views.update, name="update"),

    path('delete/<int:pk>/', views.delete, name="delete"),

    path('update2/<int:pk>/', views.update2, name="update2"),

    path('delete22/<int:pk>/', views.delete22, name="delete22"),

    path('update3/<int:pk>/', views.update3, name="update3"),

    path('delete33/<int:pk>/', views.delete33, name="delete33"),

    path('update4/<int:pk>/', views.update4, name="update4"),

    path('delete44/<int:pk>/', views.delete44, name="delete44"),

    path('payment/', views.payment, name="payment"),

    path('verification/', views.verification, name="verification"),

    path('lockin/', views.lockin, name="lockin"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter  # type: ignore
from .views import BookViewSet, BookListViewSet , ListViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"booklists", BookListViewSet)
router.register(r"lists", ListViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("opaala/", views.opaalalibrary, name="opaala"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

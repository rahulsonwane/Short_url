from django.urls import URLPattern, path

from root.views import createUrl, routeToURL


urlpatterns = [
    path('', createUrl),
    path('<slug:key>',routeToURL )
]
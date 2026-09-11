"""URL configuration for portfolio_project."""
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import FileResponse, Http404
from django.views.static import serve
import os

# Path to the frontend folder (one level up from backend/)
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend')

def serve_frontend(request):
    """Serve the frontend index.html file."""
    index_path = os.path.join(FRONTEND_DIR, 'index.html')
    if not os.path.exists(index_path):
        raise Http404("Frontend index.html not found.")
    return FileResponse(open(index_path, 'rb'), content_type='text/html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Serve frontend CSS, JS, and assets
    re_path(r'^(?P<path>css/.*)$', serve, {'document_root': FRONTEND_DIR}),
    re_path(r'^(?P<path>js/.*)$',  serve, {'document_root': FRONTEND_DIR}),
    re_path(r'^(?P<path>assets/.*)$', serve, {'document_root': FRONTEND_DIR}),
    # Serve frontend at root — must be last
    path('', serve_frontend, name='frontend'),
]

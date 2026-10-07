"""
URL configuration for core_adopt_project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# core_adopt_project/urls.py
# core_adopt_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from pets_management.views import home_view

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PetAdopt API | Panel de Control</title>
        <style>
            :root {
                --bg-color: #0f172a;
                --card-bg: #1e293b;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
                --accent: #38bdf8;
                --accent-green: #34d399;
                --border: #334155;
            }
            body {
                font-family: 'Inter', system-ui, -apple-system, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-main);
                margin: 0;
                padding: 40px 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                box-sizing: border-box;
            }
            .dashboard {
                max-width: 800px;
                width: 100%;
                background: var(--card-bg);
                border: 1px solid var(--border);
                border-radius: 16px;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
                overflow: hidden;
            }
            .header {
                padding: 30px 40px;
                border-bottom: 1px solid var(--border);
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .header h1 {
                margin: 0;
                font-size: 24px;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .status-badge {
                background: rgba(52, 211, 153, 0.1);
                color: var(--accent-green);
                border: 1px solid rgba(52, 211, 153, 0.2);
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
                display: flex;
                align-items: center;
                gap: 6px;
            }
            .status-dot {
                width: 8px;
                height: 8px;
                background: var(--accent-green);
                border-radius: 50%;
                box-shadow: 0 0 8px var(--accent-green);
            }
            .content {
                padding: 30px 40px;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .feature-card {
                background: rgba(15, 23, 42, 0.6);
                border: 1px solid var(--border);
                padding: 20px;
                border-radius: 10px;
            }
            .feature-card h3 {
                margin: 0 0 8px 0;
                font-size: 15px;
                color: var(--accent);
            }
            .feature-card p {
                margin: 0;
                font-size: 13px;
                color: var(--text-muted);
                line-height: 1.4;
            }
            .actions {
                display: flex;
                gap: 15px;
                margin-top: 20px;
            }
            .btn {
                flex: 1;
                text-align: center;
                text-decoration: none;
                padding: 12px 20px;
                border-radius: 8px;
                font-weight: 600;
                font-size: 14px;
                transition: all 0.2s ease;
            }
            .btn-primary {
                background: var(--accent);
                color: #0f172a;
            }
            .btn-primary:hover {
                background: #0ea5e9;
            }
            .btn-secondary {
                background: transparent;
                border: 1px solid var(--border);
                color: var(--text-main);
            }
            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.05);
            }
            .footer-info {
                padding: 20px 40px;
                background: rgba(15, 23, 42, 0.4);
                border-top: 1px solid var(--border);
                font-size: 12px;
                color: var(--text-muted);
                display: flex;
                justify-content: space-between;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <div class="header">
                <h1>🐾 PetAdopt API Hub</h1>
                <div class="status-badge">
                    <span class="status-dot"></span> Servidor Activo
                </div>
            </div>
            
            <div class="content">
                <p style="color: var(--text-muted); margin-top: 0; margin-bottom: 25px;">
                    Plataforma backend RESTful desarrollada bajo estándares de arquitectura limpia, control de acceso por tokens y auditoría de seguridad automatizada.
                </p>

                <div class="grid">
                    <div class="feature-card">
                        <h3>⚡ Throttling & Rate Limit</h3>
                        <p>Protección activa contra abusos con límites diferenciados para usuarios anónimos y registrados.</p>
                    </div>
                    <div class="feature-card">
                        <h3>🔒 Seguridad & Tokens</h3>
                        <p>Autenticación robusta y permisos condicionales por roles para las operaciones CRUD.</p>
                    </div>
                    <div class="feature-card">
                        <h3>📄 Paginación Global</h3>
                        <p>Optimización de respuestas JSON con bloques controlados de 10 registros por página.</p>
                    </div>
                </div>

                <div class="actions">
                    <a href="/api/pets/" class="btn btn-primary">Endpoints de Mascotas (/api/pets/)</a>
                    <a href="/admin/" class="btn btn-secondary">Panel de Administración</a>
                </div>
            </div>

            <div class="footer-info">
                <span>Stack: Django REST Framework &bull; SQLite</span>
                <span>Entorno Local Configurado</span>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pets_management.urls')),
    path('', home_view, name='home'),
]
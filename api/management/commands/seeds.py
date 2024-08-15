from django.core.management.base import BaseCommand
from api.models import User, Task, Category, Tag
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Popula la base de datos con datos de prueba en español'

    def handle(self, *args, **kwargs):
        # Crear categorías
        categorias = ['Trabajo', 'Personal', 'Hogar', 'Salud', 'Estudios']
        for nombre in categorias:
            Category.objects.create(name=nombre)

        # Crear etiquetas
        etiquetas = ['Urgente', 'Importante', 'Opcional', 'Revisión', 'Planificación']
        for nombre in etiquetas:
            Tag.objects.create(name=nombre)

        # Crear usuarios
        usuarios = [
            {'username': 'juanperez', 'email': 'juan.perez@example.com', 'first_name': 'Juan', 'last_name': 'Pérez'},
            {'username': 'maria.garcia', 'email': 'maria.garcia@example.com', 'first_name': 'María', 'last_name': 'García'},
            {'username': 'carlos.rodriguez', 'email': 'carlos.rodriguez@example.com', 'first_name': 'Carlos', 'last_name': 'Rodríguez'},
        ]
        
        for usuario_data in usuarios:
            User.objects.create_user(
                username=usuario_data['username'],
                email=usuario_data['email'],
                first_name=usuario_data['first_name'],
                last_name=usuario_data['last_name'],
                password='password123'
            )

        # Crear tareas
        tareas = [
            {'title': 'Completar informe de ventas', 'description': 'Informe de ventas mensual para la junta directiva.', 'category': 'Trabajo', 'tags': ['Urgente', 'Importante']},
            {'title': 'Llevar el coche al taller', 'description': 'Revisión anual del coche.', 'category': 'Personal', 'tags': ['Opcional']},
            {'title': 'Comprar víveres', 'description': 'Lista de la compra para la semana.', 'category': 'Hogar', 'tags': ['Planificación']},
            {'title': 'Visitar al médico', 'description': 'Chequeo general de salud.', 'category': 'Salud', 'tags': ['Revisión']},
            {'title': 'Estudiar para el examen', 'description': 'Preparación para el examen final de matemáticas.', 'category': 'Estudios', 'tags': ['Urgente', 'Planificación']},
        ]
        
        for tarea_data in tareas:
            categoria = Category.objects.get(name=tarea_data['category'])
            tarea = Task.objects.create(
                title=tarea_data['title'],
                description=tarea_data['description'],
                status=random.choice(['pendiente', 'en progreso', 'completada']),
                priority=random.choice(['baja', 'media', 'alta']),
                due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                category=categoria
            )
            for tag_name in tarea_data['tags']:
                tag = Tag.objects.get(name=tag_name)
                tarea.tags.add(tag)

        self.stdout.write(self.style.SUCCESS('Datos de prueba en español creados exitosamente.'))

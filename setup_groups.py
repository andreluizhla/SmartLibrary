from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from user.models import User

class Command(BaseCommand):
    help = 'Cria os grupos iniciais e associa permissões'

    def handle(self, *args, **kwargs):
        # Grupo Bibliotecário
        bibliotecario, created = Group.objects.get_or_create(name='Bibliotecário')
        
        # Adiciona todas as permissões ao grupo Bibliotecário
        bibliotecario.permissions.set(Permission.objects.filter(
            codename__in=[
                'gerenciar_catalogo',
                'gerenciar_emprestimos',
                'gerenciar_usuarios',
                'visualizar_catalogo',
                'acompanhar_emprestimos',
                'realizar_emprestimos',
                'editar_proprio_perfil',
            ]
        ))
        
        # Grupo Funcionário
        funcionario, created = Group.objects.get_or_create(name='Funcionário')
        funcionario.permissions.set(Permission.objects.filter(
            codename__in=[
                'visualizar_catalogo',
                'acompanhar_emprestimos',
                'editar_proprio_perfil',
            ]
        ))
        
        # Grupo Leitor
        leitor, created = Group.objects.get_or_create(name='Leitor')
        leitor.permissions.set(Permission.objects.filter(
            codename__in=[
                'visualizar_catalogo',
                'realizar_emprestimos',
                'editar_proprio_perfil',
            ]
        ))
        
        self.stdout.write(self.style.SUCCESS('Grupos criados com sucesso!'))
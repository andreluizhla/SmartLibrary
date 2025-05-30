# Generated by Django 5.2.1 on 2025-05-24 19:37

import user_reader.validar_info
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_reader", "0010_user_password_alter_user_cpf_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                help_text="Coloque uma senha com no mínimo 8 caracteres",
                max_length=100,
                validators=[user_reader.validar_info.validate_password],
                verbose_name="Senha",
            ),
        ),
    ]

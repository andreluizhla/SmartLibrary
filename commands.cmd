@REM Criar Ambiente Virtual
@REM python -m venv .venv

@REM Em seguida, TENTE o comando:
@REM .venv\Scripts\activate

@REM se ocorrer erro de permissão, execute o comando:
@REM Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

@REM Execute novamente o penúltimo comando


@REM Comandos CMD:
pip install django
pip install crispy-bootstrap5
pip install django-view-breadcrumbs
pip install black
pip install python-decouple
pip install dj-database-url

@REM Para o Backup do SQLite:
@REM python manage.py dumpdata > datadump.json

@REM Super Usuário SmartLibrary:
@REM Adm Adm
@REM ADM123

@REM Extensão Recomendada: 
@REM SQLite Viewer
@REM Black Formatter
@REM MySQL por: Database Client

@REM { 
@REM     "editor.formatOnSave": true, 
@REM     "python.formatting.provider": "black", 
@REM     "editor.defaultFormatter": "ms-python.black-formatter", 
@REM     "files.associations": { 
@REM         "**/templates/**/*.html": "django-html" 
@REM     }, 
@REM     "emmet.includeLanguages": { 
@REM         "django-html": "html" 
@REM     } 
@REM } 


@echo off
setlocal enabledelayedexpansion

set "dir_path=%~dp0"

for %%F in ("%dir_path%\migrations\*.py" "%dir_path%\migrations\*.pyc" "%dir_path%\*.sqlite3") do (
  set "filename=%%~nF"
  if not "!filename!"=="__init__" (
    del "%%F"
  )
)

echo "Deletion complete"

python manage.py makemigrations
python manage.py migrate
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin2', '', 'adminlogin')"
python populate.py

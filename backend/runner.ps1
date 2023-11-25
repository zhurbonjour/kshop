#  Создание виртуального окружения python
python -m venv .venv
#  Активация виртуального окружения
.venv/bin/activate
#  Установка всех зависимостей
cd kshop
pip install -r win-requirements.txt
# Создание миграций и их применение
python manage.py makemigrations
python manage.py migrate

Smart Remont Task

Бұл жоба екі бөліктен тұрады:

Backend: Django REST API (smart_backend/)

Frontend: Vue 3 + Tailwind + Pinia SPA (smart_frontend/)

Бұл нұсқаулық арқылы екі бөлікті де орнатып, тестілеуге болады.

1. Репозиторийді клонирлеу
git clone https://github.com/uaibol/smart_remont_task.git
cd smart_remont_task
2. Backend (Django REST API)

Виртуалды орта жасау және іске қосу:

cd smart_backend
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate # Windows

Тәуелділіктерді орнату:

pip install -r requirements.txt

Дерекқор миграцияларын жүргізу:

python manage.py migrate

Superuser жасау (админ панель үшін):

python manage.py createsuperuser

Серверді іске қосу:

python manage.py runserver

Сервер енді: http://127.0.0.1:8000/
API базалық URL: http://127.0.0.1:8000/api/

3. Frontend (Vue 3 + Tailwind + Pinia)

Node.js және npm орнатылғанын тексеру:

node -v
npm -v

Тәуелділіктерді орнату:

cd ../smart_frontend
npm install

Серверді іске қосу:

npm run serve

Фронтенд енді әдетте: http://localhost:8080/
Ол backend API-мен байланысады (http://127.0.0.1:8000/api/).

4. Backend + Frontend байланысын тексеру

Frontend бетінде өнімдер тізімі шығуы керек.

API жауап бермесе, smart_frontend/src/services/api.js ішіндегі baseURL дұрыс бапталғанын тексеріңіз:

baseURL: 'http://127.0.0.1:8000/api/',

Backend сервері қосулы екеніне көз жеткізіңіз (python manage.py runserver).

5. Админ панель (Backend)
http://127.0.0.1:8000/admin/

Superuser логинімен кіріңіз.
username: admin
password: admin123

Себеттегі өнімдер тізімі, жою мүмкіндігі.
Сатып алу сомасын көрсетеді.
Себет деректері localStorage-де сақталады.
Drag-and-drop арқылы өнімді себетке қосуға болады.




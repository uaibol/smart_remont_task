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
# Windows үшін: venv\Scripts\activate

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

Өнімдер қосып, категорияларды тексеруге болады.

6. Frontend функционалын тексеру
6.1 Product List

ProductList компоненті барлық өнімдерді тор түрінде көрсетеді.

Виртуалды скролл арқылы өнімдер көп болса жылдам жүктеу.

6.2 Product Card

Әр карточкада өнімнің суреті, атауы, бағасы және Add to Cart батырмасы бар.

Батырма карточканың оң жақ астыңғы бұрышында орналасқан.

Drag-and-drop арқылы карточканы ұстап, себетке апару мүмкіндігі бар.

6.3 Product Detail

Өнім туралы толық ақпарат көрсетіледі: сурет, сипаттама, баға, сипаттамалары.

Add to Cart батырмасы да бар.

6.4 Cart

Себеттегі өнімдер тізімі, санын өзгерту, жою мүмкіндігі.

Сатып алу сомасын көрсетеді.

Себет деректері localStorage-де сақталады.

Drag-and-drop арқылы өнімді себетке қосуға болады.

6.5 Filter Panel

Өнімдерді категория, баға және сипаттама бойынша сүзгілеу.

Сүзгі күйі URL-мен синхрондалған.

6.6 Pagination

Каталог беттерін ауыстыруға арналған навигация.

6.7 Search Bar

Іздеу енгізгенде debounce және автокомплит функциясы жұмыс істейді.

6.8 Notifications

Қате немесе сәтті әрекеттерде хабарламалар көрсетіледі (Vue Toastification немесе Pinia store арқылы).

6.9 Comparison Mode

Өнімдерді таңдап салыстыру режимі бар.

Характеристикалары таблица түрінде шығарылады.

7. Drag-and-Drop + Add to Cart

ProductCard компонентін ұстап, Cart компонентіне сүйреңіз → өнім қосылады.

Сондай-ақ Add to Cart батырмасы арқылы да қосуға болады.

UI оптимистикалық интерфейс қолданады: батырманы басқан кезде интерфейс дереу жаңартылады, егер API қатесі болса өзгеріс кері қайтарылады және хабарлама шығады.

8. SEO және SSR

Бұл жоба SPA болып табылады.

Егер SEO және SSR керек болса, Nuxt.js қолдану ұсынылады.

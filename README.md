## API Yatube - API для веб-приложения Yatube.

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
<img src="yatube_api/static/imagesicon.png" align="right" />

## Возможности API: 
- регистрация пользователей 🤷‍♂️
- получение токенов для доступа 🔑
- просмотр, публикация, редактирование, удаление записей ✍️
- комментирование записей 💬
- подписываться на авторов ❤️
- реализована пагинация 📖

## Установка 🛫

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/RaShaimardanov/api_yatube.git
```
```
cd api_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
## Примеры некоторых запросов API 🚀
|Метод   |URL                                            |Описание                       |
|:------:|:----------------------------------------------|:------------------------------|
| GET    | /api/v1/posts/                                | Получить список всех постов   |
| POST   | /api/v1/posts/                                | Добавление нового поста       |
| GET    | /api/v1/groups/                               | Получить список всех групп    |
| POST   | /api/v1/posts/{post_id}/comments/             | Добавление нового комментария |
| DELETE | /api/v1/posts/{post_id}/comments/{id}/        | Удаление комментария по id    |

Более подробная документация доступна после запуска проекта по адресу: 📄
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
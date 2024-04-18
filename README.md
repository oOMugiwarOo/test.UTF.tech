# About the project

Тестовое задание для UTF.tech 

## Установка и запуск

Для запуска проекта вам понадобятся Docker и Docker Compose. Если они не установлены на вашем компьютере, установите их в соответствии с официальной документацией Docker и Docker Compose.

1. Создайте файл .env в корневом каталоге проекта и установите необходимые переменные окружения. Например:
    ```bash
	POSTGRES_DB=postgres
	POSTGRES_USER=postgres
	POSTGRES_PASSWORD=postgres
	POSTGRES_HOST=postgres
	POSTGRES_PORT=5432
	```

2. Запустите Docker контейнеры и соберите проект:

    ```bash
	docker-compose up -d --build
    ```

3. Создайте суперпользователя (администратора):

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. Перейдите по адресу http://localhost:8000/admin/ и войдите, используя учетные данные суперпользователя, чтобы добавить данные о продуктах и другие необходимые настройки.
   
5. Документация Swagger доступна по адресу http://localhost:8000/api/v1/.

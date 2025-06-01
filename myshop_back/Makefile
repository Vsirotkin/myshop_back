# Makefile для Django-проекта

# Путь к manage.py
MANAGE = python src/manage.py

help:
	@echo "Доступные команды:"
	@echo "  makemigrations - Создать миграции"
	@echo "  migrate        - Применить миграции"
	@echo "  run            - Запустить сервер разработки"
	@echo "  createsuperuser - Создать суперпользователя"
	@echo "  clean          - Очистить миграции и БД"
	@echo "  resetdb        - Сбросить БД и применить миграции заново"

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run:
	$(MANAGE) runserver

createsuperuser:
	$(MANAGE) createsuperuser

clean:
	rm -f src/db.sqlite3
	rm -rf src/shop/migrations/000*.py
	@echo "Очистка завершена: удалены миграции и база данных."

resetdb: clean migrate
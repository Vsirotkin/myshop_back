# Makefile

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
	@echo "  test           - Запустить все тесты shop"
	@echo "  test-one       - Запустить конкретный тест"
	@echo "                 make test-one ARGS=shop.tests.test_views.ViewTests.test_product_list_view"
	@echo "  coverage       - Запустить тесты с анализом покрытия"

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

test:
	$(MANAGE) test shop.tests

test-one:
	$(MANAGE) test $(ARGS)

coverage:
	python -m coverage run --source=src/shop src/manage.py test shop.tests
	python -m coverage report -m
	python -m coverage html
	@echo "HTML отчет сохранён в htmlcov/index.html"
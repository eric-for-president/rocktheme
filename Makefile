# Makefile for Django project (Linux)

PYTHON = python3
MANAGE = $(PYTHON) manage.py

help:
	@echo "Available commands:"
	@echo "  make run         -> Run Django development server"
	@echo "  make migrate     -> Apply database migrations"
	@echo "  make makemig     -> Create new migrations"
	@echo "  make shell       -> Open Django shell"
	@echo "  make createsuper -> Create superuser"
	@echo "  make test        -> Run tests"
	@echo "  make clean       -> Remove __pycache__ and *.pyc"

run:
	$(MANAGE) runserver 0.0.0.0:8000

migrate:
	$(MANAGE) migrate

makemig:
	$(MANAGE) makemigrations

shell:
	$(MANAGE) shell

createsuper:
	$(MANAGE) createsuperuser

test:
	$(MANAGE) test

clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

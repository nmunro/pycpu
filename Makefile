.PHONY: build clean clean-docker clean-docs docs repl test shell run lint dev-tools-check logs poetry lock
.DEFAULT_GOAL: build

REPORT := $(or $(REPORT),report -m)
GIT_CHANGED_PYTHON_FILES := $(shell git diff --name-only -- '***.py')
DEV_TOOLS := $(and $(shell which docker git))
COMPOSE_FILE := 'docker-compose.yml'
RUNNING_CONTAINERS := $(shell docker ps -a -q -f name="spectrum-*")
SERVICE := $(or $(SERVICE),pycpu)
SRC := $(or $(SRC),.)

# define standard colors
ifneq ($(TERM),)
    GREEN        := $(shell tput setaf 2)
    RESET        := $(shell tput sgr0)

else
    GREEN        := ""
    RESET        := ""

endif

dev-tools-check:
ifeq ($(DEV_TOOLS),)
	$(error Some of your dev tools are missing, unable to proceed)
endif

build: dev-tools-check
ifeq ($(FORCE),true)
	@docker container rm -f $(SERVICE)
	@docker container prune
endif
	@docker compose -f $(COMPOSE_FILE) build $(SERVICE)

run: dev-tools-check
	@docker compose -f $(COMPOSE_FILE) up $(SERVICE) --remove-orphans

lint:
ifeq ($(SERVICE),pycpu)
	@$(foreach file, $(GIT_CHANGED_PYTHON_FILES), $(shell docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) /bin/bash -c "poetry run black ${file} && poetry run isort ${file} && poetry run flake8 ${file}"))
else
	$(error Command not available for service: '$(SERVICE)')
endif

repl: dev-tools-check
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run python manage.py shell --settings=spectrum.settings.dev

shell:
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) /bin/bash

test: dev-tools-check
	@rm -rf coverage
ifneq ($(and $(TEST-CASE),$(SRC)),)
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage run --source=$(SRC) --branch ./manage.py test --settings=spectrum.settings.test --no-input $(TEST-CASE); docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage $(REPORT)
else ifneq ($(SRC),)
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage run --source=$(SRC) --branch ./manage.py test --settings=spectrum.settings.test --no-input; docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage $(REPORT)
else ifneq ($(TEST-CASE),)
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage run --branch ./manage.py test --settings=spectrum.settings.test --no-input $(TEST-CASE) --parallel
else
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry run coverage run --branch ./manage.py test --settings=spectrum.settings.test --no-input --parallel
endif
	@rm -rf .coverage.*

clean:
	@docker container prune -f

ifeq ($(IMAGES),true)
	@docker image prune -fa
	@docker builder prune -fa
endif

ifeq ($(VOLUMES),true)
	@docker volume prune -fa
endif

ifeq ($(SYSTEM),true)
	@docker system prune -fa
	@docker builder prune -fa
endif

logs:
	@docker compose -f $(COMPOSE_FILE) logs -f $(SERVICE)

poetry:
ifeq ($(SERVICE),pycpu)
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry $(CMD)
else
	$(error Command not available for service: '$(SERVICE)')
endif

requirements:
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) poetry export -f requirements.txt -o requirements.txt

lock: dev-tools-check
ifeq ($(SERVICE),pycpu)
	@[ ! -d "poetry.lock" ] && rm poetry.lock || true
	@docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE) /bin/bash -c "poetry lock --no-update"
else
	$(error Command not available for service: '$(SERVICE)')
endif

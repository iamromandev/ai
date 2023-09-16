# system
.PHONY: clean
clean:
	docker system prune -a --force
	docker volume prune --force

.PHONY: ps
ps:
	docker compose ps -a

# local
.PHONY: build
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
up:
	docker-compose -f docker-compose.yml up -d

.PHONY: stop
stop:
	docker-compose -f docker-compose.yml stop

.PHONY: down
down:
	docker-compose -f docker-compose.yml down

.PHONY: restart
restart:
	make stop
	make build
	make up

# deploy
.PHONY: deploy
deploy:
	python src/manage.py tailwind build

# deploy
.PHONY: test
test:
	poetry run python src/manage.py test apps.dictionary.tests

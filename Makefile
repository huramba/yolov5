include .env
main: ver rt push
rotate: ci rt push
# npm install watch-cli -g
# watch:
# 	watch -p 'src/**/*' -c 'make stop run-srv'
ver:
	docker run --rm -it -v `pwd`/.env:/src/.env $(REG)/ci/gulp:$(GULP) ver
ci rt:
	docker-compose build $@
push pull down logs ps:
	docker-compose $@
	
R=docker-compose run --rm
run-rt:
	$R rt
run-ci:
	$R ci

run-dev:
	docker-compose up -d ci bash

up:
	docker-compose up -d rt

sh:
	docker-compose run --rm ci bash

C='default commit message'
commit:
	git add .; git commit -m '$C'; git push

V=-v `pwd`/src:/srv

.PHONY: debug
debug:
	docker run --rm -ti \
	--name ddd \
	--network cims \
	-p 8765:8765 \
	$V \
  	-v `pwd`/debug:/root/.vscode-server-insiders \
	$(REG)/ci/$(SRV):$(CI) \
	bash
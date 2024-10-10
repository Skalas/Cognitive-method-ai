up:     ## Crea los servicios (PostgreSQL)
	docker-compose up -d --build

up-dev: ## Crea los servicios (PostgreSQL) en modo desarrollo
	docker-compose up --build --watch

up-db:  ## Levanta solo la base de datos (PostgreSQL)
	docker-compose up -d db

down:   ## Detiene y remueve los servicios (PostgreSQL)
	docker-compose down -v

start:  ## Inicia los servicios (PostgreSQL)
	docker-compose start

stop:   ## Apaga los servicios (PostgreSQL)
	docker-compose stop

test:
	docker-compose exec app pytest /app/tests

deploy-stage:
	docker build -f ./app/Dockerfiles/Dockerfile.prod --platform="linux/amd64" -t us-central1-docker.pkg.dev/${PROJECT_ID}/ai-api/metodocognitivo:dev ./app
	docker push us-central1-docker.pkg.dev/${PROJECT_ID}/ai-api/metodocognitivo:dev
	# gcloud run deploy metodocognitivo-api --allow-unauthenticated \
	# 	--min-instances=25 --max-instances=25 --region=us-east1 --platform=managed \
	# 	--image=us-east1-docker.pkg.dev/$PROJECT_ID/medlm-api/medlm-api:dev \
	# 	--memory 4Gi \
	# 	--cpu 2 \
	# 	--project ${PROJECT_ID}

deploy-prod:
	docker build -f ./app/Dockerfiles/Dockerfile.prod --platform="linux/amd64" -t us-east1-docker.pkg.dev/g-prd-gsv000-tlmd-erp-prj-6fe2/medlm-befe/medlm-api:prod ./app
	# docker push us-east1-docker.pkg.dev/g-prd-gsv000-tlmd-erp-prj-6fe2/medlm-befe/medlm-api:prod
	# gcloud run deploy medlm-api --allow-unauthenticated \
	# 	--min-instances=25 --max-instances=25  --region=us-east1 --platform=managed \
	# 	--image=us-east1-docker.pkg.dev/g-prd-gsv000-tlmd-erp-prj-6fe2/medlm-befe/medlm-api:prod \
	# 	--memory 4Gi \
	# 	--cpu 2 \
	# 	--project g-prd-gsv000-tlmd-erp-prj-6fe2


help: # Tomado de http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: help up down stop start up-dev deploy

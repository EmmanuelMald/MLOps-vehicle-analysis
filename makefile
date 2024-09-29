co2-build-image:
	docker build -t co2_estimator -f co2_estimator/deployment/co2_emissions.dockerfile .

autonomy-build-image:
	docker build -t autonomy_estimator -f autonomy_estimator/deployment/autonomy_estimator.dockerfile .

co2-run-container:
	docker run -p 5000:5000 co2_estimator

autonomy-run-container:
	docker run -p 4000:4000 autonomy_estimator

autonomy-build-docker-registry:
	echo $(DOCKER_PSSWD) docker login -u $(DOCKER_USERNAME) --password-stdin 
	docker build -t autonomy_estimator -f autonomy_estimator/deployment/autonomy_estimator.dockerfile .
	docker tag autonomy_estimator $(DOCKER_USERNAME)/$(AUTONOMY_DOCKER_REPO):latest
	docker push $(DOCKER_USERNAME)/$(AUTONOMY_DOCKER_REPO):latest

co2-build-docker-registry:

	echo $(DOCKER_PSSWD) docker login -u $(DOCKER_USERNAME) --password-stdin 
	docker build -t co2_estimator -f autonomy_estimator/deployment/autonomy_estimator.dockerfile .
	docker tag autonomy_estimator $(DOCKER_USERNAME)/$(AUTONOMY_DOCKER_REPO):latest
	docker push $(DOCKER_USERNAME)/$(AUTONOMY_DOCKER_REPO):latest


co2-build-image:
	docker build -t co2_estimator -f co2_estimator/deployment/co2_emissions.dockerfile .

autonomy-build-image:
	docker build -t autonomy_estimator -f autonomy_estimator/deployment/autonomy_estimator.dockerfile .

co2-run-container:
	docker run -p 5000:5000 co2_estimator

autonomy-run-container:
	docker run -p 4000:4000 autonomy_estimator
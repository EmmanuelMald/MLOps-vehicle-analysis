co2-build-image:
	docker build -t co2_estimator -f co2_estimator/deployment/co2_emissions.dockerfile .

co2-run-container:
	docker run -p 5000:5000 co2_estimator
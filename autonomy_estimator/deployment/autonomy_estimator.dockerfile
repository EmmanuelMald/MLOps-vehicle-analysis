FROM python:3.11

# create the main directory where everything will
# be stored
WORKDIR /app

# Copy the pyproject.toml in the current directory
COPY pyproject.toml poetry.lock ./

#Install poetry to be used in the dockerfile
RUN pip install poetry==1.8.3

# Install dependencies without creating a virtual env
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy all the co2_estimator folder into the workdir
COPY autonomy_estimator/. . 

# Specify the port where the app will listen
EXPOSE 4000

# executing gunicorn to run the endpoint where the model will be consumed
CMD ["gunicorn", "-w", "4", "-b","0.0.0.0:4000", "deployment.api:app"]
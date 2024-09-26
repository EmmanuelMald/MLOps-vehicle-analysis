FROM python:3.11

# create the main directory where everything will
# be stored
WORKDIR /app

# Copy all the root file into the workdir
COPY . .

#Install poetry to be used in the dockerfile
RUN pip install poetry

# Install dependencies without creating a virtual env
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Specify the port where the app will listen
EXPOSE 5000

CMD ["python", "include/scripts/api.py"]
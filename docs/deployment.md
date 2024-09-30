# ***Model Deployment***

This steps were followed for each ML model:

## ***Save a trained model***

Once the model has been proved to give the expected accuracy, it is needed to save it.

To do so, *joblib* was used, which is a Python library that helps to save Python objects. It is especially efficient with large numpy arrays, making it faster than the standard pickle module for scientific computing tasks.

## ***Endpoint to consume the model***

The model to be consumed in production needs an endpoint to query the saved model and deliver the prediction. In this project, an API was created using *Flask*, which is a web framework to develop web applications, APIs, and microservices; Is know by its ease of use and high customization. 

## ***Containerize the endpoint***

Once the API has proven that works as expected, its time to containerize it. To do so, *docker* was used to create an image of the API, and then store it in *DockerHub*. Once the image is store there, it can be pulled by anyone and be used in docker. Nevertheless, we want to deploy this image on a server in order to create a url that everyone can use, without the need of using docker.

## ***Deployment to Render***

*Render* is a fully managed cloud platform that provides hosting services for web applications, APIs, static websites, databases, and more. It offers a free tier, making it a great option for personal projects or testing out deployments before scaling up to paid plans.

It has integration with docker, so any image can be pulled from it and then being used by the server.

This last step is crutial due to this server delievers a world-wide url, which you can access to request predictions to the your saved model. 

In this case, a manual deployment was implemented, nevertheless, it can also use CICD to improve the automation to productionize your models.





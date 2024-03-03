
## Cost control app

This is a simple income and expense tracking application project.
There is a frontend that provides the main functionality, as well as an API interface for obtaining additional ones. The service also includes registration.

### Applied technologies:
- Django
- Django ORM
- DRF
- PostgreSQL
- Docker/Docker-compose
- Kubernetes


## Usage

This application can be deployed in two versions:

### Using Kubernetes
You just need to reconfigure volumes to the required folders or create them first. You also need to configure ingress based on your host, Next, in the root directory you need to run the command:

```
 kubectl apply -f .
```

### Using Docker-Compose 
In this option it is enough to build the project

```
docker-compose build
```

and in next step you can see your service in localhost:8000
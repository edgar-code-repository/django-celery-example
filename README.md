CELERY EXAMPLE APP (WITH RABBITMQ)
---------------------------------------------------------------------------------------------------------------------

Sencilla aplicación desarrollada con Django 2.2 y Celery 4.3 que 
muestra un pequeño ejemplo de ejecución de una tarea asincrónica.

La aplicación utiliza RabbitMQ como broker de mensajería.

**Configuración de Celery en archivo settings para utilizar RabbitMQ como broker:**

```

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'

```

---------------------------------------------------------------------------------------------------------------------

Pantalla desde donde se gatilla llamada a tarea celery:

![Screenshot 1](screenshots/celery_call_with_rabbitmq.png)


Pantalla de respuesta que indica id de la tarea generada:

![Screenshot 2](screenshots/celery_response_with_rabbitmq.png)


Ejecución de la tarea gatillada:

![Screenshot 3](screenshots/task_execution_with_rabbitmq.png)


---------------------------------------------------------------------------------------------------------------------


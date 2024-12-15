
# Django CBV DRF TodoApp

A comprehensive Django project showcasing the use of Class-Based Views (CBVs) and Django REST Framework (DRF) to build a functional Todo application. This repository is perfect for developers looking to understand the integration of CBVs and DRF in a Django application.

## Features

- **Class-Based Views (CBVs)** for efficient and reusable code.
- RESTful API implementation using Django REST Framework.
- Endpoints for creating, retrieving, updating, and deleting tasks.
- Example serializers and viewsets for managing data.
- Structured project organization for easy scalability and maintenance.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shahramsamar/Django_CBV_DRF_TodoApp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Django_CBV_DRF_TodoApp
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application at `http://127.0.0.1:8000/`.

2. Use the RESTful API endpoints to manage tasks. Examples:
   - `GET /api/tasks/`: Retrieve a list of tasks.
   - `POST /api/tasks/`: Create a new task.
   - `PUT /api/tasks/<id>/`: Update an existing task.
   - `DELETE /api/tasks/<id>/`: Delete a task.

3. Explore CBV implementations for learning how to structure reusable views.

## Example

### Task Model
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

### API ViewSet
```python
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

### Serializer
```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

## Requirements

- Python 3.7+
- Django 3.2+
- Django REST Framework 3.12+

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

- **Author**: Shahramsamar
- **Email**: [shahramsamar2010@gmail.com](mailto:shahramsamar2010@gmail.com)
- **GitHub**: [Shahramsamar](https://github.com/shahramsamar)
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")

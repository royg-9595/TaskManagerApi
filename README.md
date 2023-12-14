# Task Management API using Django REST
### Objective: 
Create a RESTful API for a task management system using Django Rest Framework. The API
should support CRUD operations (Create, Read, Update, Delete) for tasks.
### Requirements:
1. ***Task Model:***
- Create a model for tasks with the following fields:
- Title (CharField)
- Description (TextField)
- Due Date (DateField)
- Status (ChoiceField: Pending, In Progress, Completed)
1. ***API Endpoints:***
- Create API endpoints for the following CRUD operations:
- List all tasks
- Retrieve a single task by ID
- Create a new task
- Update an existing task
- Delete a task
1. ***Authentication:***
- Implement token-based authentication for the API. Ensure that only authenticated users
can perform CRUD operations
1. ***Permissions:***
- Implement permissions to ensure that users can only update or delete tasks that they
own.

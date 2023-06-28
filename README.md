# Task Manager

This project is a REST API built with Django, Postgres, and Docker, providing CRUD operations for tasks and progress tracking.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Authentication and Authorization](#authentication-and-authorization)
- [Database Design](#database-design)
- [Functionalities](#functionalities)
- [Contributing](#contributing)

## Introduction

Welcome to the REST API project! This API allows users to manage tasks, track progress, and perform CRUD operations. It's built using Django framework, Postgres as the database, and Docker for containerization.

## Technologies Used

This project utilizes the following technologies:

| Technology  | Description                          |
|-------------|--------------------------------------|
| Django      | Python web framework                  |
| Postgres    | Relational database management system |
| Docker      | Containerization platform             |

## Features

- CRUD operations: Users can create, read, update, and delete tasks.
- Progress Tracking: Tasks can be marked as completed or in progress.
- Authentication and Authorization: Secure endpoints requiring user authentication.
- Custom Permissions: Different levels of access for authenticated users.
- Email Functionalities: Sending emails for user-related actions (e.g., password reset).

## Installation

To set up the project locally, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python manage.py makemigration` and `python manage.py migrate`

## Authentication and Authorization

The project implements authentication and authorization for secure access to API endpoints. Users need to authenticate using their credentials to obtain an access token. The access token must be included in the request headers for authorized requests.

## Database Design

The project includes a database with more than 10 entities. The database schema is designed to support task management and progress tracking functionalities. It consists of tables for users, tasks, progress, and other related entities.

## Functionalities

- User Registration
- Password Reset
- CRUD Operations

## Contributing

Contributions to the project are welcome! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

Please adhere to the coding conventions and guidelines specified in the project.

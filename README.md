# Python Backend Best Practices Project

## Introduction
This project is a reference implementation of a Python backend, showcasing best practices in API design, testing, and deployment. It serves as a guideline for developing robust and scalable backend services within our organization.

## Features
- **Proto Interface Description**: Implements Protocol Buffers for defining data structures and service interfaces.
- **OpenAPI API Definition**: Utilizes OpenAPI specifications for a clear and standardized RESTful API description.
- **Connexion & Flask**: Leverages Connexion with Flask for a spec-first approach to API development.
- **CI/CD Pipeline**: Integrates Continuous Integration and Continuous Deployment using Jenkins on Kubernetes.
- **Versioned & Iterative Migrations**: Manages database schema changes efficiently and safely.
- **Unit Testing**: Incorporates extensive unit tests to ensure code quality and reliability.
- **Acceptance Testing**: Implements acceptance tests to validate functionality against business requirements.
- **User & Authentication Service**: Provides a dedicated service for user management and authentication.
- **JWT Generation**: Implements JSON Web Tokens for secure data transmission.
- **Authorization Middlewares**: Ensures secure access control within the application.

## Workspace

Either using vscode devcontainer or Docker 

```bash
cd docker 
./build-dev.sh
docker compose up
```

## Running locally

```bash
python3 -m src.cmd.start
```

## Running acceptance tests
```bash
python3 -m unittest discover ./src/tests/acceptance
```


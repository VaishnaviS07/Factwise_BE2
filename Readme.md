# Team Project Planner Tool

## Overview

A Django-based API for managing users, teams, and project forums. It affords functionalities to create, list, describe, and update users and groups, as well as manipulate task boards and duties.

## Features

- User Management: Create, list, describe, and replace customers.
- Team Management: Create, listing, describe, and update groups. Add and eliminate users from groups.
- Project Board Management: Create and near forums, add and update obligations, and export forums.

## Though Process
- Use of Django and DRF: Chose Django for its robustness in building web programs and Django REST Framework (DRF) for developing and managing RESTful APIs efficaciously.
- Local File Storage: Decided to apply JSON files for patience to simplify garage and retrieval while not having a database setup. This is good enough for the assignment's scope and keeps the setup sincere.
- Clear Abstractions: Implemented base lessons for users, teams, and project boards, and prolonged them with concrete classes. This modular approach guarantees clear separation of concerns and makes the code greater maintainable.
- Error Handling: Incorporated proper mistakes coping with to make sure the API responds gracefully to invalid inputs and different errors, improving person experience and reliability.
- Constraints: Enforced precise constraints and bounds on names and outlines to maintain facts integrity and keep away from excessively large inputs.
  
## API Endpoints

### User Management

- **Create a User**: `POST /api/customers/`
- **List All Users**: `GET /api/customers/`

### Team Management

- **Create a Team**: `POST /api/groups/`
- **List All Teams**: `GET /api/teams/`

### Project Board Management

- **Create a Project Board**: `POST /api/assignment-forums/`
- **List All Project Boards for a Team**: `GET /api/undertaking-boards/`

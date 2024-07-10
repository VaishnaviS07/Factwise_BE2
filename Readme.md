# Team Project Planner Tool

## Overview

A Django-based API for managing users, teams, and project forums. It affords functionalities to create, list, describe, and update users and groups, as well as manipulate task boards and duties.

## Features

- User Management: Create, list, describe, and replace customers.
- Team Management: Create, listing, describe, and update groups. Add and eliminate users from groups.
- Project Board Management: Create and near forums, add and update obligations, and export forums.

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

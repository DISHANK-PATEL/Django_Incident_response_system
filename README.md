Incident Response & Alert Management Backend
============================================

Overview
--------

This project implements a production-oriented backend system for reporting, managing, and resolving operational incidents through a structured workflow. The system enables users to submit incident reports with supporting media, while administrators and responder teams manage assignments, status transitions, and updates.

The platform emphasizes traceability, modular architecture, and operational metrics through audit logging, responder coordination, and SLA tracking. It is designed to mirror real-world backend challenges such as permission enforcement, workflow integrity, media handling, and performance measurement.

Implemented Features
--------------------

### Authentication & Authorization

*   User registration
    
*   JWT-based authentication
    
*   Role-aware permission handling
    
*   Token refresh support
    

### Incident Management

*   Incident creation and modification
    
*   Status lifecycle enforcement
    
*   Severity classification
    
*   Location and category metadata
    
*   Incident deletion controls
    

### Timeline & Updates

*   Chronological incident updates
    
*   Update attribution tracking
    
*   Dedicated timeline retrieval endpoint
    

### Media Handling

*   Attachment upload via API
    
*   Persistent media storage
    
*   File URL access through responses
    

### Responder Coordination

*   Responder team creation and management
    
*   Assignment-ready schema
    
*   Full CRUD operations for teams
    

### Filtering & Sorting

*   Keyword filtering
    
*   Category/location filtering
    
*   Severity-based sorting
    
*   Unresolved incident queries
    

### SLA Metrics

*   Aggregated performance statistics
    
*   Acknowledgement timing analysis
    
*   Resolution timing analysis
    
*   Severity/category breakdowns
    

### Audit Logging

*   Status transition tracking
    
*   Actor attribution
    
*   Historical status reconstruction
    

### Testing

*   Workflow integrity validation
    
*   Metrics correctness verification
    
*   Permission enforcement checks
    
*   Media handling validation
    

---
## Technology Stack

| Category            | Technologies Used              |
|---------------------|--------------------------------|
| **Backend Framework** | Python, Django, Django REST Framework |
| **Infrastructure**    | Docker, Docker Compose        |
| **Database**          | MySQL                         |
| **Authentication**    | JWT Token Authentication      |
| **Documentation**     | OpenAPI / Swagger             |
| **Testing**           | Django Test Framework         |

## Project Structure
---
```

Django_Incident_response_system/
|
├── incident_response/      # Project configuration
├── incidents/              # Incident workflow and metrics
├── responders/             # Responder team logic
├── users/                  # Authentication and user model
├── media/                  # Uploaded files
|
├── dockerfile              # Container definition
├── docker-compose.yml      # Orchestration config
├── requirements.txt        # Python dependencies
├── manage.py               # Django entry point
└── README.md               # Documentation
```
Setup Instructions
------------------
## Prerequisites
Make sure you have the following installed:
- Docker
- Docker Compose

---
```bash
git clone https://github.com/DISHANK-PATEL/Django_Incident_response_system.git
```
## Start Services
Build and start the containers:

```bash
docker-compose build
docker-compose up
```

---

## Management Commands
Run commands inside the container using:

```bash
docker-compose run exec python manage.py <command>
```

### Apply Migrations
```bash
docker-compose run exec python manage.py migrate
```

### Create Superuser
```bash
docker-compose run exec python manage.py createsuperuser
```

### Run Tests
```bash
docker-compose run exec python manage.py test
```

---

### API Base URL
http://localhost:8000/

### Swagger Documentation
http://localhost:8000/api/docs/

---
## API Endpoints
<img width="1095" height="533" alt="image" src="https://github.com/user-attachments/assets/9e8fd04b-21a8-44a5-96a6-9572545d9baf" />
<img width="1096" height="542" alt="image" src="https://github.com/user-attachments/assets/10df6b23-2e7b-4099-bfa7-44f5d93c6127" />

---
## Learning Objectives Demonstrated

This project showcases practical experience and applied understanding in the following areas:

- Designing scalable REST APIs  
- Structuring modular Django applications  
- Implementing role-based access control  
- Managing complex workflow state transitions  
- Maintaining audit history integrity  
- Building media upload pipelines  
- Creating advanced query interfaces  
- Aggregating SLA operational metrics  
- Containerizing production-style environments  
- Writing meaningful automated tests  
- Producing professional documentation  

---




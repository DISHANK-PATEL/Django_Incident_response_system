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
---

## Sample Screenshots

### 1. Creating a User
<img src="https://github.com/user-attachments/assets/f7a7e9b9-58a4-4a70-acb8-5806de915e88" alt="Creating User" width="100%" />

---

### 2. Login via JWT Authentication
<img src="https://github.com/user-attachments/assets/7464a0cd-9d0b-4216-8b71-e16f26745e3a" alt="JWT Login" width="100%" />

---

### 3. Admin Creating a Responding DevOps Team
<img src="https://github.com/user-attachments/assets/d60489a1-e90e-41e5-a405-99cd9f80c129" alt="Admin Creating DevOps Team" width="100%" />

---

### 4. User Reporting an Incident with Image Evidence
<img src="https://github.com/user-attachments/assets/900c4486-d059-4a8e-8b3a-c7c8a9536277" alt="User Reporting Incident" width="100%" />

---

### 5. Viewing the Uploaded Incident Image
<img src="https://github.com/user-attachments/assets/1e8f5fe7-a06b-45ce-ac46-e80fc5b542c8" alt="Viewing Uploaded Image" width="100%" />

---

### 6. Admin Assigning a Responding Team to the Incident
<img src="https://github.com/user-attachments/assets/673bbdd8-20d6-4a58-8bcc-154646275a7e" alt="Assigning Team" width="100%" />

---

### 7. Responder Changing the Incident Status
<img src="https://github.com/user-attachments/assets/6d8fd64a-af84-498f-af3b-5acdfc3134df" alt="Changing Status" width="100%" />

---

### 8. Checking the Timeline of an Incident
<img src="https://github.com/user-attachments/assets/f9699eef-ec4d-4297-82a2-86d5008ad61b" alt="Incident Timeline" width="100%" />

---

### 9. Viewing SLA Metrics
<img src="https://github.com/user-attachments/assets/83c268ef-2289-4365-82be-5767884a7d1b" alt="SLA Metrics" width="100%" />

---

### 10. Displaying All Incident Details Sorted by Severity
<img src="https://github.com/user-attachments/assets/d1ee76bf-7be5-4d1d-9054-e6339388cc60" alt="Incidents Sorted by Severity" width="100%" />

---

### 11. Advanced Filtering Based on Specifications
<img src="https://github.com/user-attachments/assets/f19fc117-615f-4608-93a9-d1c8ae3a9971" alt="Advanced Filtering" width="100%" />



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




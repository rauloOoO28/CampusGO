# CampusGO
🇺🇸 English
📖 Description

The Campus Navigation System is an application designed to help students, staff, and visitors find routes within a university campus quickly and efficiently.

The system models the campus as a graph, where:

Nodes represent buildings or important locations.
Edges represent paths between locations.
Each connection has a weight representing the distance.

The shortest path is calculated using Dijkstra's algorithm.

The backend is built with Django, while the frontend uses HTML, CSS, and JavaScript to display the map and routes.


**🎯 Project Goals**
Facilitate navigation within the campus.
Apply graph theory concepts.
Implement efficient routing algorithms.
Build a clean architecture between frontend and backend.
Develop a scalable and well-documented system.


**🧠 Technologies Used**
Backend
Django
Python
REST API
Implementation of Dijkstra's algorithm
Frontend
HTML
CSS
JavaScript
Interactive map visualization
Version Control
Git
GitHub


**🏗️ Project Architecture**
The project is divided into several main modules:
  campus-navigation-system
    │
    ├── backend_servidor
    ├── frontend_interfaz
    ├── datos_sistema
    ├── documentacion_proyecto
    ├── pruebas_sistema
    └── scripts_utilidad


**Backend**
_Contains:_
  API
  route calculation logic
  graph model
  pathfinding algorithm
  

**Frontend**
_Contains:_
  user interface
  campus map
  route visualization


**System Data**

Contains the campus graph model:
    _datos_sistema/grafo_campus.json_


**📊 Graph Model**
The campus is represented as a graph where:
Each node represents a location.
Each edge represents a path between locations.
Weights represent distances between nodes.


**👥 Development Team**

This project is developed by a two-person team, working collaboratively on:

  backend development
  frontend development
  graph modeling
  algorithm implementation

The project uses Git and GitHub for collaborative development.

**📌 Features**
Campus graph representation
Shortest path calculation
Route visualization on map
API for route queries
Modular and scalable architecture


**🚀 Project Status**

*Currently under development.*





## ProjectPilot Pro
#### A Project Management Application

The purpose of this project is to allow for managing projects and tasks in a large organization where there are different departments, team leads and tasks that are assigned. The project is mostly tailored for Software Engineering teams but then, other non-software establishments can use them


## Usecase Scenario
Company ABC wants a centralised way of organising teams for projects, assigning tasks and keeping track of the time members take to complete their tasks.


## Features
#### 1. User Registration and Login: 
Conveniently, there are two kinds of users. ``Workers`` and ``Team Leads``.

1.1 Register a User
* Implement a user registration system allowing individuals to sign up as either "Workers" or "Team Leads".
* Collect necessary information during registration (e.g., username, password, email).

1.2 User Login
* Implement a secure login system to authenticate users based on their credentials.
* Distinguish between "Workers" and "Team Leads" during the login process.


#### 2. Departments and Projecs
2.1 Create Department
* Develop functionality for "Team Leads" to create departments.
* Include fields for department name, description, and other relevant information.

2.2 CRUD Operations on Departments
* Enable "Team Leads" to perform CRUD operations on departments (Create, Read, Update, Delete).

2.3 Project Creation
* Implement project creation within departments.
Include details such as project name, description, start date, and end date.

#### 3. Joining Departments
3.1 Worker Joining a Department
* Allow "Workers" to join existing departments.
* Display a list of available departments for "Workers" to choose from.

3.2 Assignment to Projects
* When a "Worker" joins a department, they can be assigned to a specific project within that department by a "Team Lead".

#### 4. Tasks
4.1 Task Creation
* Allow "Team Leads" to create tasks within projects.
* Include task details like name, description, due date, and priority.

4.2 Task Assignment
* Enable "Team Leads" to assign tasks to "Workers" within their department.

4.3 Task Progress Tracking
* Implement a system for both "Team Leads" and "Workers" to track the progress of tasks.
* Include features like task status (e.g., not started, in progress, completed), time tracking, and comments.

#### 5. Additional Features
5.1 Notifications
* Implement a notification system to inform users about task assignments, updates, and approaching deadlines.

5.2 Reporting
* Develop reporting functionalities for both "Team Leads" and "Workers" to view statistics, task completion rates, and overall project progress.



## TODO CheckList
These are the list of tasks to be done for this project to be completed. They will be checked as they are tackled

- [x] Register a user and login (workers and team leads)

* Team Lead Responsibilities
- [x] Create Department
- [x] CRUD Operations on Departments
- [x] Project Creation
- [x] Task Creation
- [x] Task Assignment
- [ ] Task Progress Tracking

* Workers Responsibilities
- [x] Join a department and can only read it
- [ ] View tasks they have been assigned to

* Additional Features
- [ ] Notifications
- [ ] Reporting
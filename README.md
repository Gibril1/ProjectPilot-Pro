## TASKMgt

The purpose of this project is to allow for managing projects and tasks in a large organization where there are different departments, team leads and tasks that are assigned. The project is mostly tailored for Software Engineering teams but then, other non-software establishments can use them


## Usecase Scenario
Company ABC wants a centralised way of organising teams for projects, assigning tasks and keeping track of the time members take to complete their tasks.


## Features
* User Registration and Login: Conveniently, there are two kinds of users. ``Workers`` and ``Team Leads``.

Conveniently, team leads are supposed to take care of the administration of projects and their timelines.

* Department and Projects: This involves performing CRUD operation on these resources. Department could be more of a team, for software engineering establishments or generic departments as it is found in other companies.

* Joining Departments: Once a department is created, workers can join these departments. And when you are in a department, you are assigned to a project that a team leads wants you on

* Tasks: These are the main tasks that are created by team leads and assigned to users. From here, team leads get to assign these tasks to users and track their progress


## TODO
These are the list of tasks to be done for this project to be completed. They will be crossed as they are tackled

1. Register a user and login (workers and team leads)
2. Team Leads can
* Create a department and perform other write operations on it
* Create tasks and assign them
* Check for progress of tasks
3. Workers can
* Join a department and can only read it
* View tasks they have been assigned to
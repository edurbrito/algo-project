## Algorithmics Project 2021/2022

# K-D Trees for Space Indexing on Large Employment Databases

Eduardo Brito & Gular Samadova & Elvin Mirzazada

> ---

## Overview

The goal of this project is to model a database of employees, in a large company, and then to query the database in order to find the best people to create a team for a new project idea. 

All the employees are categorized by their set of skills - a set of k coordinates in a k-dimensional space. 

Using Space Indexing methods such as K-D Trees it is possible to efficiently implement a range search and find the best matching / nearest people to work together in a new task or project.

> See the report [here](docs/poster.pdf).

--------------------------------

## Instructions

For Windows:

Open a terminal:
1. Create the Virtual Environment: `py -m venv env`
2. Activate the Virtual Environment: `.\env\Scripts\activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the application with `py src`

For Linux:

Open a terminal:
1. Create the Virtual Environment: `python -m venv env`
2. Activate the Virtual Environment: `source env/bin/activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the application with `python src`
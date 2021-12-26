# Roles are assigned binary values - True or False
# Skills are assigned integer values - between 0 to 100

TECH_ROLES = """Chief of Technology
Systems Manager
Network Manager
Database Administrator
Software Developer
Tester
Quality Assurance Analyst
Web Developer
Penetration Tester
Data Scientist""".split("\n")

OTHER_ROLES = """Chief Executive
Client Support Manager
Operations Manager
Sales Manager
Financial Manager
Human Resources Manager
Project Manager
Product Manager
Marketing Specialist
Designer
Recruiter""".split("\n")

LANGUAGES="""English
Spannish
French
German
Russian
Portuguese""".split("\n")

PROGRAMMING="""HTML
CSS
Bootstrap
Tailwind.css
Javascript
Python
C
C++
Java
React
Vue
PHP
Flutter
SQL
NoSQL
PostgreSQL
MySQL
R
Dart""".split("\n")

SYSTEMS="""Linux
Flask
Django
Laravel
Node.js
Git
Docker
Kubernetes
Android
IOS
AWS
Azure""".split("\n")

OTHER = """Office Suit
Agile
Google Analytic
Blender
Photoshop
Video Editing
Graphic Design
Filming
Professional Writing
Communication
Negotiation
Speaking
Management
Team working
Critical Thinking
Coordination""".split("\n")

COLUMNS = TECH_ROLES + OTHER_ROLES + LANGUAGES + PROGRAMMING + SYSTEMS + OTHER
# Selenium Grid Optimizer

**Student Name:** Pranav Gaikwad  
**Course:** DevOps (CSE3253)  
**Project Category:** Testing  
**Project Title:** Selenium Grid Optimizer – Optimize Selenium Grid Resource Allocation  

---

##  Project Overview

### Problem Statement  
Inefficient resource allocation in Selenium Grid leads to uneven load distribution, where some nodes remain idle while others are overloaded. This results in increased test execution time and poor utilization of available infrastructure.

### Objective  
The objective of this project is to design and implement an optimization mechanism that intelligently distributes test execution across Selenium Grid nodes to improve performance and resource utilization.

---

##  Key Features

- Parallel test execution using Selenium Grid  
- Load imbalance identification in default execution  
- Round-robin based test scheduling  
- Smart resource-based scheduling using Selenium Grid API  
- Dynamic browser selection (Chrome/Firefox)  
- Improved node utilization and reduced execution time  

---

##  System Architecture
Test Scripts (Python)
│
▼
Selenium Grid Hub (Port 4444)
│
┌───────────────┬───────────────┐
▼ ▼ ▼
Chrome Node Firefox Node Additional Nodes
(Docker) (Docker) (Scalable)

---

## Technology Stack

### Core Technologies
- Programming Language: Python  
- Automation Tool: Selenium WebDriver  

### DevOps Tools
- Containerization: Docker  
- Orchestration: Selenium Grid  
- Version Control: Git  

---

### Prerequisites
- Docker installed  
- Python 3.x installed  
- Git installed  

---


1. Clone the repository:

git clone https://github.com/your-username/selenium-grid-optimizer.git

cd selenium-grid-optimizer

Install dependencies:
pip install -r requirements.txt

Start Selenium Grid:

cd infrastructure/docker

docker compose up -d

Open Selenium Grid UI:
http://localhost:4444

### Test Execution
1. Basic Test
python tests/test_google.py

2. Parallel Execution
python tests/parallel_test.py

3. Round-Robin Optimizer
python tests/optimizer_test.py

4. Smart Optimizer (Resource-Based)
python tests/smart_optimizer.py

### Optimization Techniques
1. Default Execution

Sends all tests to a single browser

Causes load imbalance

2. Round-Robin Scheduling

Alternates between Chrome and Firefox

Ensures equal distribution

3. Resource-Based Scheduling (Advanced)
Uses Selenium Grid API:
http://localhost:4444/status

Detects free slots dynamically

Assigns test to least loaded node


# AI-Powered Client Onboarding & Proposal Generation Agent

I've built a **hybrid automation** project, that is, mixing custom python code with low-code/no-code platforms to solve a business problem. This system acts as a bridge between messy business processes and concrete AI solutions.

Generally, when a company requests a new software system, they usually provide an unstructured "project brief". Reading through this document takes time and may lead to human error. The purpose of this project is to automate that exact process. 

Following phases are the step-by-step procedure to get started: 

## Phase 1: Problem Definition & Architecture Design 

<div align = "center"> <h3>Process Flow </h3>
<img width="1256" height="751" alt="image" src="https://github.com/user-attachments/assets/d2a32055-8b88-431b-8e7d-8cf138f5684a" /> </div>
<br>
<br>

## Phase 2: Core AI Processing Stack (Python & Custom Code)

Firstly, the libraries inside '[requirements.txt](requirements.txt)' cover the API stack, document handling and AI framing. 

We'll use Pydantic to ensure our LLM reads unstructured text and structures it into a JSON format. The code '[schemas.py](app/schemas.py)' defines three distinct Pydantic models. They work like nesting dolls, where the smaller models are placed inside the larger one. 

**1. TechnicalRequirement** (The Smallest Model) 
<br>
This model structures a single technical need.
- *category*: A string indicating where the tech belongs.
- *details*: A string explaining the specific tech.

**2. FeatureItem**
<br>
This model structures a single software feature.
- *name*: The features' name.
- *description*: What it does
- *estimated_complexity*: A difficulty rating

**3. StructuredProjectBrief** (The Master Model)
<br>
This is the main container holding everything. It uses regular data types alongside lists.
- *client_name*: A single string for the client's name.
- *project_goals*: A standard Python list of strings for objectives.
- *technical_stack*: A list of TechnicalRequirement ojbects.
- *core_features*: A list of FeatureItem objects.
- *estimated_weeks*: A single integer representing the timeline.

The '[config.py](app/config.py)' is the configuration python file. This establishes the connection to both open AI (gpt-4o-mini) and n8n workflow.

This '[ai_engine.py](app/ai_engine.py)' reads an uploaded raw PDf, extracts its text, and parses it into our structured data model using OpenAI's Structured Outputs feature.

Finally, our API Endpoints and automation dispatcher '[main.py](app/main.py)' ties everything together. It hosts an endpoint to accept documents, runs the extraction, and instantly fires off the structured JSON payload to a low-code webhook. 

## Phase 3: Low-Code Automation Design

Now that our script outputs valid JSON to a webhook, we configure the visual workflow inside n8n. To build this automation n8n, we'll create a 3-node linear workflow that captures incoming webhook data, generates a personalized document from a template, and broadcasts the completion message to the team.

<div align = "center"> <h3> Workflow Automation</h3>
<img width="928" height="362" alt="image" src="https://github.com/user-attachments/assets/314e472b-c985-40c7-bb38-e886fde94d10" /> </div>
<br>
<br>

**1. The Trigger**: Custom Webhook Receiver
<br>
- Add a Webhook node to n8n canvas, and this node acts as our listener.

**2. The Action**: Google Docs Template Generator
<br>
- Add a Google Docs node and connect it directly to our Webhook node.

**3. The Notification**: Slack 
<br>
- Add a Slack node and connect it to the output of the Google Docs node. 

<div align = "center"> <h3>Team announcement on Slack triggered</h3>
<img width="1561" height="781" alt="image" src="https://github.com/user-attachments/assets/1e4b5da9-51a3-4dfb-b2e9-f91fab718cb8" /> </div>
<br>
<br>

## Phase 4: Swagger UI testing control center

We start our local sever instance after `python app/main.py` . After that we navigate to our local browser at `http://127.0.0`. This reveals the interactive Swagger testing control center. 

<div align = "center"> <h3> Swagger UI </h3>
<img width="902" height="826" alt="image" src="https://github.com/user-attachments/assets/de41631a-2be7-4869-a459-4f0036b1656a" /> </div>
<br>

Subsequently, `open the /api/v1/analyze-board` route block, click **Try it out**, drop an unstructured project description text file saved as a PDf, and click **Execute**. 




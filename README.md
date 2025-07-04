
# FlowGen AI: Queries to Actionable Steps—Effortlessly! 🚀

- [Live Link](https://flowgenai.streamlit.app/)  

# Problem Statement

Technical teams and developers often face inefficiencies when translating complex tasks into executable workflows. Manual breakdowns of technical queries into code, diagrams, and step-by-step processes are time-consuming, prone to inconsistency, and difficult to scale. This leads to:

- Delayed project timelines due to ambiguous task definitions.

- Knowledge silos where critical implementation logic isn’t standardized.

- Repetitive work in documenting workflows for recurring tasks.

FlowGen AI addresses these challenges by automating the conversion of technical requirements into clear, executable plans.

# Solution

FlowGen AI is an AI-powered workflow generator that transforms vague technical queries into structured, ready-to-implement execution plans. Built on Groq's Gemma2-9B-It model and Streamlit, it offers:

- Step-by-Step Decomposition: Breaks tasks into numbered, logic-driven steps with purpose descriptions.

- Workflow Visualization: Generates process diagrams using ASCII art or Mermaid.js for clarity.

- Code Generation: Provides modular, commented code snippets (Python or other languages).

- Markdown Output: Delivers results in developer-friendly formatting for easy integration into documentation.

The tool acts as a collaborative partner for developers, DevOps teams, and technical managers, streamlining workflows from ideation to implementation.



# Impact

- 10x Faster Planning: Reduce hours of manual brainstorming to seconds.

- Standardized Processes: Ensure consistency across team workflows.

- Scalable Knowledge Transfer: Create reusable templates for recurring tasks.

- Developer Empowerment: Focus on coding instead of documentation.


# Usage Guide
1. Describe Your Task: Input technical requirements (e.g., "Build a real-time sentiment analysis API using FastAPI")

2. Generate Workflow: Click 🚀 Generate Execution Steps

3. Receive Output:

- Structured implementation steps

- Visual workflow diagram

- Ready-to-use code snippets

- Library/technology recommendations
# Installation Guide
## Prerequisites

- Python 3.9 or higher

- Groq API key

## Steps To Run Locally

1. Clone the Repository:

```bash
   git clone https://github.com/your-repo/flowgen-ai.git  
   cd flowgen-ai     
```
2. Create a Virtual Environment (recommended for dependency isolation):
```bash
   python -m venv venv  
   source venv/bin/activate  # For Windows: venv\Scripts\activate  
```
3. Install Dependencies:
```bash
   pip install -r requirements.txt  
```
4.  Launch the Application:

```bash
   streamlit run app.py  
```


5. Access the Interface:

- Open http://localhost:8501 in your browser.

- Enter Groq API key in the sidebar

- Note: Replace your-repo in the clone command with your repository URL.


## Key Features
- Dynamic Workflow Adaptation: Handles tasks ranging from data pipelines to cloud infrastructure setup.

- Tech Stack Agnostic: Generates solutions for Python, JavaScript, DevOps tools, and more.

- Collaboration-Ready Output: Markdown formatting enables direct copy-paste into project docs.

## Transform Ambiguity into Action. Accelerate Technical Execution.

Note: Requires valid Groq API key. Customize system prompts in main.py for domain-specific workflows.

## Authors

- [@Aansh Garg](https://github.com/ANSH2736)


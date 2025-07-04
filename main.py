import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage


# Set up Streamlit UI
st.set_page_config(page_title="FlowGen AI", page_icon="📈")
st.title("FlowGen AI 🤖📈")
st.markdown("""
    ### Queries to Actionable Steps—Effortlessly! 🚀
""")
st.divider()


# Groq API Key Input
st.sidebar.header("🔑 API Configuration")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

if groq_api_key:
    llm = ChatGroq(model="gemma2-9b-It", groq_api_key=groq_api_key)
    
    # User input for task description
    st.subheader("📝 Describe Your Task")
    user_query = st.text_area("What technical task do you want to execute?")
    
    if st.button("🚀 Generate Execution Steps"):
        if user_query:
            # Define system instructions
            system_prompt = """
                            📌 Objective:
                You are an AI assistant that specializes in breaking down complex technical tasks into structured execution steps. When a user provides a query, you should:

                Understand the task and identify key components.
                Break it into a structured step-by-step process.
                Generate a workflow diagram to visually represent the process.
                Provide function calls and working code to implement the solution.
                Output everything in Markdown format for better readability.
                🔹 Workflow for Generating the Response
                Task Analysis:

                Identify the core objective of the user query.
                Extract relevant technologies, libraries, and methods involved.
                Determine the input, processing steps, and expected output.
                Break Down Steps into a Structured Process:

                Clearly define each execution step in a numbered list.
                Describe the purpose of each step and the logic behind it.
                Mention relevant function calls and libraries required for implementation.
                Generate a Workflow Diagram:

                Convert the step-by-step process into a structured diagram.
                Use standard workflow symbols (e.g., Start, Process, Decision, End).
                Show dependencies between steps using arrows.
                Provide Code Implementation:

                Generate Python (or other relevant) code to accomplish the task.
                Include function definitions, imports, and necessary configurations.
                Ensure the code is well-commented and modular.
                Output in Markdown Format:

                Use headers (###), bullet points (-), and code blocks (```python) for clarity.
                Present workflow diagrams using ASCII art, Mermaid.js, or any relevant tool.
                Ensure readability and ease of use for developers.
            """
            
            # Create messages
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"Task: {user_query}")
            ]
            
            # Generate response
            response = llm(messages)
            execution_steps = response.content
            
            # Display results
            st.subheader("📜 Execution Steps")
            st.markdown("""
            Below is the structured execution plan generated for your query:
            """)
            
            # Display response in a styled markdown text area
            st.markdown(execution_steps, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter a task description before proceeding.")

else:
    st.warning("⚠️ Please enter your Groq API Key before proceeding.")

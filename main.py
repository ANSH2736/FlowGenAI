import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# Streamlit page config
st.set_page_config(page_title="FlowGen AI", page_icon="📈")

st.title("FlowGen AI 🤖📈")
st.markdown("### Queries to Actionable Steps—Effortlessly! 🚀")
st.divider()

# Sidebar API key input
st.sidebar.header("🔑 API Configuration")
groq_api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")

if groq_api_key:

    # Initialize Groq model (stable model)
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=groq_api_key
    )

    # User input
    st.subheader("📝 Describe Your Task")
    user_query = st.text_area("What technical task do you want to execute?")

    if st.button("🚀 Generate Execution Steps"):

        if user_query:

            system_prompt = """
📌 Objective:
You are an AI assistant that specializes in breaking down complex technical tasks into structured execution steps.

Instructions:
1. Understand the user task.
2. Break it into clear numbered steps.
3. Generate a workflow diagram.
4. Provide working Python code.
5. Format everything in clean Markdown.

Output format:
### Task Breakdown
Step-by-step execution plan.

### Workflow Diagram
ASCII or Mermaid diagram.

### Code Implementation
Provide clean Python code with comments.
"""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"Task: {user_query}")
            ]

            try:
                response = llm.invoke(messages)
                execution_steps = response.content

                st.subheader("📜 Execution Steps")
                st.markdown("Below is the structured execution plan generated for your query:")
                st.markdown(execution_steps)

            except Exception as e:
                st.error(f"Error generating response: {e}")

        else:
            st.warning("⚠️ Please enter a task description before proceeding.")

else:
    st.warning("⚠️ Please enter your Groq API Key before proceeding.")
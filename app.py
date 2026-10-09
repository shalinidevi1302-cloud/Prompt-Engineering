import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt
st.set_page_config(
    page_title="Qwen Prompting Techniques",
    page_icon="🤖",
    layout="centered"
)
st.title("🤖 Qwen Prompting Techniques")
st.write(
    "Select a prompting technique, enter your task, "
    "and generate a response using the Qwen LLM."
)
technique = st.selectbox(
    "Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)
task = st.text_area(
    "Enter your task:",
    placeholder=(
        "Example: Explain the difference between "
        "AI and Machine Learning."
    )
)
temperature = st.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)
max_tokens = st.slider(
    "Maximum Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=100
)
if st.button("Generate Response"):
    if task.strip() == "":
        st.warning("Please enter a task.")
    else:
        try:
            final_prompt = build_prompt(
                technique,
                task
            )
            st.subheader("Generated Prompt")
            st.code(
                final_prompt,
                language="text"
            )
            with st.spinner(
                "Qwen is generating the response..."
            ):
                answer = generate_response(
                    final_prompt,
                    temperature,
                    max_tokens
                )
            st.write(answer)
        except Exception as e:
            st.error(
                f"Error while generating response: {e}"
            )
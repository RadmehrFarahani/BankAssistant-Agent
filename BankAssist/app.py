import streamlit as st 

from langchain_ollama import OllamaLLM

from data import examples, prefix, suffix

from langchain_core.example_selectors import LengthBasedExampleSelector

from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate


##################################################################################

# UI 

st.set_page_config(
    page_title="Bank Assistant",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Welcome To The Bank Assistant System")

st.header("Hey, How can I help you?")

form_input = st.text_area("Enter text", height=300)

tasktype_option = st.selectbox(
    "Please select the banking service?",
    (
        "Account & Balance",
        "Money Transfer",
        "Card Services",
        "Loans & Credit",
        "Transactions",
        "Security & Fraud",
        "Personal Information",
        "Online Banking",
        "Branch Services",
        "General Banking"
    ),
    key="task_type"
)

numberOfWords = st.slider("words limit", 1, 200, 25)

submit = st.button("Generate")

#################################################################################################

#BackEnd

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.9
)


example_template = """
Question : {question}

Answer : {answer}
"""


example_prompt = PromptTemplate(
    input_variables=['question', 'answer'],
    template=example_template
)


example_selector = LengthBasedExampleSelector(
    example_prompt=example_prompt,
    max_length=500, #Increase this number make a lot more examples
    examples=examples
)


fewShotTemp = FewShotPromptTemplate(
    prefix=prefix,
    suffix=suffix,
    example_prompt=example_prompt,
    example_selector=example_selector,
    input_variables=['input', 'tasktype_option']
)


st.write(
    llm.stream(
        fewShotTemp.format(
            input=form_input,
            tasktype_option=tasktype_option
        )
    )
)
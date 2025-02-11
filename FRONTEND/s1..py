from langchain_groq import ChatGroq
import streamlit as st
def correct_grammar(text):
    llm = ChatGroq(
        model="gemma2-9b-it",
        temperature=0,
        groq_api_key="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"  # Replace with your actual API key
    )
    
    prompt = f"Check the grammar of the following text. If it's correct, return it as is. If it has grammar mistakes, correct them without changing the meaning or adding extra words. Also, list the incorrect words and provide feedback on what went wrong.\nText: {text}"
    
    response = llm.invoke(prompt)  # Get AIMessage object
    corrected_text = response.content  # Extract actual text
    
    if corrected_text.strip() == text.strip():
        return text, "Sentence is already correct:"
    else:
        incorrect_words_feedback =""
        
        # The response from the model should ideally contain the list of incorrect words and feedback
        if "incorrect words" in corrected_text.lower():
            # Extract incorrect words and explanations (assuming response structure includes it)
            incorrect_words_feedback = extract_incorrect_words(corrected_text) 
        return corrected_text, incorrect_words_feedback

def extract_incorrect_words(response_text):
    # Implement logic to parse incorrect words and their explanations from the response
    # This will depend on how the LLM outputs feedback, here assuming a simplified approach
    incorrect_words = []
    lines = response_text.splitlines()
    for line in lines:
        if "incorrect" in line.lower():
            incorrect_words.append(line.strip())
    return incorrect_words

st.title("Simple LLM Grammar Checker")

input_text = st.text_area("Enter a sentence to check grammar:")
if st.button("Check Grammar"):
    corrected_text, feedback = correct_grammar(input_text)
    st.write("### Corrected Text:")
    st.write(corrected_text)
    if feedback:
        st.write("### Incorrect Words and Feedback:")
        st.write(feedback)
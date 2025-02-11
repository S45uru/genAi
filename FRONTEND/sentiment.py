from langchain_groq import ChatGroq
llm=ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)
def analyze_sentiment_and_suggest(text):
    prompt = f"Analyze the sentiment of the following text and suggest improvements to make it more positive.\nText: {text}"
    response = llm.invoke(prompt)
    return response.content
    st.title("simple LLM sentiment analysis")
    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment_and_suggest(input_text)
        st.write("### Sentiment Analysis:")
        st.write(sentiment)
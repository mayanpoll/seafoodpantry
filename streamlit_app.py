import streamlit as st
import google.generativeai as genai
import pandas as pd

# Load secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# Load CSV data
@st.cache_data
def load_product_data():
    return pd.read_csv("SeafoodWatch_data_full.csv")
    
product_data_df = load_product_data()
product_data_string = product_data_df.to_string(index=False)


# Define rules
rules = """
You are a seafood sustainability expert from Seafood Watch and you have to recommend seafood based on environmental impact and tell consumers whether they need to buy or avoid the seafood type and reason why.
Be cordial at all times.
If consumers haven't chosen yet, recommend alternatives or certified seafood type.
Offer recommendations if consumers are undecided between the seafood type available.
Based on the consumer's preference or past questions, you may suggest a specific seafood type they might consider environmentally sustainable.
After selecting a seafood type, confirm whether they should buy or avoid the seafood type, and ask if they have any further questions.
When decided whether to buy the seafood type, provide a summary of the conversation, including the seafood type, recommendation, origin, fishing gear, and farming method.
If the seafood type and/or location is not in the list, say that it is not in the Seafood Watch database that you know. If the seafood type does exist in the list but in another location than the consumer has asked about, you can still talk about the list.
After saying something about the list, you may still recommend whether to buy or avoid the seafood type from the place that the consumer asked about.
If user ask you for recipe for a certain seafood, find some recipe online if you don't know.
Below is your environmentally sustainable seafood type recommendation with a reason based on the information discussed.
"""

# Initialize chat history with the system message
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": f"{rules}\n\nSeafood Database:\n{product_data_string}"},
                                   {"role": "assistant", "content": "Hello! How can I help you with sustainable seafood?"}]

st.title("Seafood Watch Chatbot 🐟")
st.markdown("Ask me anything about sustainable seafood!")

def fetch_messages(messages, model="gemini-1.5-flash", temperature=0):
    formatted_messages = [{"role": msg["role"], "parts": [{"text": msg["content"]}]} for msg in messages if msg["role"] != "system"] # Exclude system role from the main message list
    gemini_model = genai.GenerativeModel(model)
    try:
        response = gemini_model.generate_content(formatted_messages, generation_config={"temperature": temperature})
        return response.text
    except Exception as e:
        return f"Sorry, there was an error communicating with the AI: {e}"

# Display chat history (skipping the initial system message for display)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Create the context for the API call, including the initial system message
    context = st.session_state.messages

    with st.spinner("Thinking..."):
        bot_response = fetch_messages(context, temperature=0.7)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.chat_message("assistant").write(bot_response)
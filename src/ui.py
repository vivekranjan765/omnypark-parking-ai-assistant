import os
import shutil
import streamlit as st
from app import RAGAssistant, load_documents


st.set_page_config(
    page_title="OmnyPark Public Parking Assistant",
    page_icon="🚗",
    layout="centered"
)


@st.cache_resource
def initialize_assistant():
    """
    Initialize the RAG assistant once and cache it.
    """
    assistant = RAGAssistant()
    docs = load_documents()
    assistant.add_documents(docs)
    return assistant


def reset_vector_db():
    """
    Optional helper to clear ChromaDB during development.
    """
    chroma_path = "chroma_db"
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)


def main():
    st.title("🚗 OmnyPark Public Parking Assistant")
    st.caption("Ask about parking charges, free hours, validation rules, weekends, and public holiday policies.")

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! I can help with parking charges, free hours, "
                    "cinema validation, weekend parking, and public holiday rules."
                ),
            }
        ]

    # Initialize assistant
    try:
        assistant = initialize_assistant()
    except Exception as e:
        st.error(f"Error initializing assistant: {e}")
        st.stop()

    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_question = st.chat_input("Ask a parking question...")

    if user_question:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = assistant.invoke(user_question)
                except Exception as e:
                    answer = f"Sorry, an error occurred: {e}"

                st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})

    # Sidebar
    with st.sidebar:
        st.header("Sample Questions")
        st.markdown("- What are the parking charges per hour?")
        st.markdown("- How many free hours do I get?")
        st.markdown("- Can cinema visitors get extra parking time?")
        st.markdown("- Is parking free on weekends?")
        st.markdown("- Is parking free on public holidays?")
        st.markdown("- Where can I validate my parking?")

        st.divider()

        if st.button("Clear Chat"):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": (
                        "Hello! I can help with parking charges, free hours, "
                        "cinema validation, weekend parking, and public holiday rules."
                    ),
                }
            ]
            st.rerun()


if __name__ == "__main__":
    main()
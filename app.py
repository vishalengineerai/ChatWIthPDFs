import streamlit as st
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.memory.buffer import ConversationBufferMemory
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from HT import bot_template, user_template, css
import PyPDF2

# Function to extract text from uploaded PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text 

# Function to split the extracted text into chunks
def get_text_chunks(text, chunk_size=1000):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to convert text chunks into embeddings
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(text_chunks, embeddings)
    return vectorstore

# Function to create a conversation chain for querying the vector store
def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite', temperature=0)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input and generate responses
def handle_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With Your PDFs Docs", page_icon=":smiley:", layout="wide")

    st.write(css, unsafe_allow_html=True)

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = None

    st.header('Chat with multiple PDFs :books: ')
    user_question = st.text_input('Ask a question about your PDFs')
    if user_question:
        handle_user_input(user_question)
    
    with st.sidebar:
        st.subheader('Your documents')
        pdf_docs = st. file_uploader(
            'Upload your PDFs here and click on the "Process"      button', type=['pdf'], accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                # Get the PDFs Text
                raw_text = get_pdf_text(pdf_docs)

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text) 

                # Vector Store
                vector_store = get_vectorstore(text_chunks)

                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)

if __name__ == "__main__":
    main()  
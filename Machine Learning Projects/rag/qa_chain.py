from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from config import Config


def create_qa_chain(vector_store):

    if vector_store is None:
        return None

    llm = ChatGroq(
        api_key=Config.GROQ_API_KEY,
        model=Config.LLM_MODEL,
        temperature=Config.TEMPERATURE,
    )

    prompt_template = """
Use the following pieces of context to answer the question.

If you don't know the answer, just say that you don't know.
Do not make up an answer.

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=[
            "context",
            "question",
        ],
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": Config.SEARCH_K,}),
        chain_type_kwargs={"prompt": prompt,},
        return_source_documents=True,
    )

    return qa_chain

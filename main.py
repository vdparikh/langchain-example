from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import LlamaCppEmbeddings
from sys import argv
from langchain.chains import RetrievalQA

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All


texts = [
    "Security by design is a concept that emphasizes the importance of incorporating security measures into the design and development of systems, applications, and products from the very beginning of the process. It aims to integrate security as a fundamental part of the development lifecycle, rather than treating it as an afterthought or add-on.",
    "The idea behind security by design is to minimize the risk of security vulnerabilities and threats by designing products and systems with security in mind from the start. This means considering security requirements and best practices at every stage of the design and development process, from the initial planning and architecture design to the final testing and deployment."
]

persist_directory = 'db_1'
llama = LlamaCppEmbeddings(model_path="./models/ggml-model-q4_0.bin",n_ctx = 1024, n_threads=64, n_batch=1024)

db = Chroma(persist_directory=persist_directory, embedding_function=llama)

def ingest():
    for t in texts:
        print(t)

    db.add_texts(texts)
    db.persist()
    #db = None

    print("ingestion completed")


    #db = Chroma.from_documents(texts, llama, persist_directory=persist_directory)

def query(q): 
    print(q)

    #db = Chroma(persist_directory=persist_directory, embedding_function=llama)

    #llama = LlamaCppEmbeddings(model_path=model)

    retriever = db.as_retriever(search_kwargs={"k": 1})

    callbacks = [StreamingStdOutCallbackHandler()]

    llm = GPT4All(model="./models/ggml-gpt4all-j-v1.3-groovy.bin", backend='gptj', callbacks=callbacks, verbose=False)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

    print("sending query")
    res = qa(q)
    answer, docs = res['result'], res['source_documents']

    print(answer)
    return answer


#ingest()
query("What is security engineering")

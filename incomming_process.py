import pandas
import joblib
import requests
import numpy as np
import faiss
try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate



def icopro(querry):
    def create_embedding(text_list):
        r = requests.post("http://localhost:11434/api/embed",json={
            'model':'bge-m3',
            'input':text_list 
        })

        embedding=r.json()['embeddings']
        return embedding


    def inference(prompt):
        r = requests.post('http://localhost:11434/api/generate', json={
            'model':'llama3.2',
            'prompt':prompt,
            'stream':False

        })
        response= r.json()
        
        return response


    df = joblib.load('embedding.joblib')

    incoming_query = querry#input('ask a question')

    embeded_question = create_embedding(incoming_query)[0]

    # Build FAISS index from existing bge-m3 embeddings and perform vector similarity search
    corpus_embeddings = np.vstack(df['embedding']).astype('float32')
    faiss.normalize_L2(corpus_embeddings)

    dimension = corpus_embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(corpus_embeddings)

    query_vector = np.array([embeded_question], dtype='float32')
    faiss.normalize_L2(query_vector)

    top_result = 6
    _, indices = index.search(query_vector, top_result)
    max_idx = indices[0]
    new_df = df.iloc[max_idx]

    # LangChain PromptTemplate to construct prompt with context and question
    prompt_template = PromptTemplate(
        template="""I am teaching web development in my Sigma web development course. Here are video subtitle chunks containing video title, 
    video number, start time in seconds, end time in seconds, the text at that time:

    {context}
    ---------------------------------
    "{question}"
    User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you)
      where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. 
      If user asks unrelated question, tell him that you can only answer questions related to the course.and convert the seconds into minutes .
      you should also provide a summy of the topic
    """,
        input_variables=["context", "question"]
    )

    context_json = new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")
    prompt = prompt_template.format(context=context_json, question=incoming_query)

    response=inference(prompt)['response']

    return response






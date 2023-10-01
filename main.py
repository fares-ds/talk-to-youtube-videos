from fastapi import FastAPI
from langchain_helper import create_vdb_from_youtube_url, get_response_from_query

app = FastAPI()

@app.post("/ask")
def ask_video(video_url: str, question: str):
    db = create_vdb_from_youtube_url(vidoe_url=video_url)
    output = get_response_from_query(db=db, query=question, k=4)
    return output

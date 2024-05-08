from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from services.genai import (
    YoutubeProcessor,
    GeminiProcessor
)
                            

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    #advanced settings

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

genai_processor = GeminiProcessor(
    model_name= "gemini-pro",
    project = "mission-dynamo" # Google Cloud Project ID
)

@app.post("/analyze_video")
def analyze_video(request: VideoAnalysisRequest):
    # Doing the analysis


    processor = YoutubeProcessor(genai_processor = genai_processor)
    result = processor.retrieve_youtube_documents(str(request.youtube_link), verbose = True)

    # Check summary
    #summary = genai_processor.generate_document_summary(result, verbose = True)

    # Find key concepts
    key_concepts = processor.find_key_concepts(result, verbose = True)
    return {
        "key_concepts": key_concepts
    }

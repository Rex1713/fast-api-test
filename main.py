from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Mini SHL Recommender API")

# Simulated mock data
mock_data = [
    {
        "assessment_name": "Cognitive Ability Test",
        "remote": "Yes",
        "adaptive": "No",
        "duration": "20 mins",
        "type": "Cognitive",
        "url": "https://example.com/assessment1"
    },
    {
        "assessment_name": "Personality Questionnaire",
        "remote": "Yes",
        "adaptive": "Yes",
        "duration": "15 mins",
        "type": "Personality",
        "url": "https://example.com/assessment2"
    },
]

@app.get("/recommend")
async def recommend_assessments(query: str = Query(..., description="Text query or URL")):
    # Just return mock data and fake summary
    summary = "- Cognitive tests measure thinking skills\n- Personality tests assess traits"
    return {
        "results": mock_data,
        "summary": summary
    }

@app.get("/health")
async def health_check():
    return {"status": "ok"}

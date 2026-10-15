from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
import requests
from app.ai_engine import AIEngine
from app.config import settings

app = FastAPI(title="Brainlake AI Automation Pipeline", version="1.0")
ai_engine = AIEngine()

def dispatch_to_low_code_workflow(payload: dict):
    """Asynchronously triggers the low-code engine to maintain swift API performance."""
    if not settings.MAKE_WEBHOOK_URL:
        print("[Warning] No Webhook URL set. Automation dispatch skipped.")
        return
    try:
        response = requests.post(settings.MAKE_WEBHOOK_URL, json=payload, timeout=10)
        print(f"[Automation Status] Webhook response received: {response.status_code}")
    except Exception as e:
        print(f"[Automation Error] Failed to hand off data to low-code environment: {str(e)}")

@app.post("/api/v1/analyze-onboard")
async def onboard_client(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid format. Please upload a PDF file.")
    
    # Read the file data securely
    file_bytes = await file.read()
    
    # 1. Parse text from the PDF
    extracted_text = ai_engine.extract_text_from_pdf(file_bytes)
    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="The provided PDF document appears empty or unreadable.")
    
    # 2. Structure the data using the AI engine
    structured_data = ai_engine.analyze_brief(extracted_text)
    
    # Convert Pydantic object directly into a standard Python dict
    serialized_payload = structured_data.model_dump()
    
    # 3. Offload external API calls (Make/n8n/Slack) onto a background thread
    background_tasks.add_task(dispatch_to_low_code_workflow, serialized_payload)
    
    return {
        "status": "Success",
        "message": "AI analysis complete. Core proposal engine dispatched downstream.",
        "data": serialized_payload
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

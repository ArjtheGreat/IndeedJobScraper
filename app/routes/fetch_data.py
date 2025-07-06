from api.data_processor import process_job_data
from fastapi.responses import JSONResponse
from fastapi import APIRouter

router = APIRouter()

@router.get("/get-job-data")
def fetch_job_data():
    job_count_json = process_job_data()
    
    return JSONResponse(content={"counts": job_count_json}, status_code=200)
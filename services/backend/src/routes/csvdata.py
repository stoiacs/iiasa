import time

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile
from tortoise.transactions import in_transaction

import src.crud.users as crud
from src.auth.jwthandler import get_current_user
from src.schemas.users import UserOutSchema
from src.database.models import CSVData

router = APIRouter()


@router.get("/csv-data", dependencies=[Depends(get_current_user)])
async def get_data(variable: str, item: str, scenario: str):
    if not variable: return JSONResponse(content={"error": "Missing Variable."}, status_code=422)
    if not item: return JSONResponse(content={"error": "Missing Item."}, status_code=422)
    if not scenario: return JSONResponse(content={"error": "Missing Scenario."}, status_code=422)
    return await CSVData.filter(Variable=variable, Item=item, Scenario=scenario).order_by('Year').values()


@router.get("/csv-data/params", dependencies=[Depends(get_current_user)])
async def get_params(scenario: str = None, item: str = None):
    result = {}
    if scenario:
        result["items"] = list(
            map(lambda x: x["Item"], await CSVData.filter(Scenario=scenario).distinct().values('Item')))
    if item:
        result["variables"] = list(
            map(lambda x: x["Variable"], await CSVData.filter(Item=item).distinct().values('Variable')))
    return result


@router.post("/csv-data", dependencies=[Depends(get_current_user)])
async def upload_data(file: UploadFile, current_user: UserOutSchema = Depends(get_current_user)):
    if file.filename.endswith('.csv'):
        data_to_save = []
        # batch is is the current timestamp
        batchId = int(time.time())
        contents = await file.read()
        lines = contents.decode().split("\n")
        for lineNum, line in enumerate(lines):
            columns = line.strip().split(',')
            if lineNum > 0 and len(columns) == 8:  # skip header and check if all columns are present
                row_to_save = CSVData(
                    BatchId=batchId,
                    Model=columns[0],
                    Scenario=columns[1],
                    Region=columns[2],
                    Item=columns[3],
                    Variable=columns[4],
                    Year=int(columns[5]),
                    Unit=columns[6],
                    Value=float(columns[7] or 0)
                )
                data_to_save.append(row_to_save)
        print(f"Saving {len(data_to_save)} records to database")
        await CSVData.bulk_create(data_to_save)
        print("Data saved successfully")
        return JSONResponse(content={"message": "CSV data uploaded and saved successfully"})
    else:
        return JSONResponse(content={"error": "Invalid file format. Only CSV files are allowed."}, status_code=400)

import sys, os
import sys, os
from fastapi import HTTPException
from backend.paths import DB_FILE


from datetime import date
from fastapi import FastAPI
from backend import db_helper
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Expense(BaseModel):

    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date:date
    end_date:date


@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses (expense_date:date):
    expenses=db_helper.get_expenses_for_date(expense_date)
    return expenses

@app.post("/expenses/{expense_date}")
def post_expenses (expense_date:date,expenses:List[Expense]):
   db_helper.delete_expense_for_a_date(expense_date)
   for expense in expenses:
       db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
   return {"message":"expenses updated successfully"}

@app.post("/analytics_by_category/")
def get_analytics(date_range:DateRange):
    print("DEBUG: endpoint called")
    print("Start date:", date_range.start_date)
    print("End date:", date_range.end_date)
    ...
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    print("DEBUG data fetched:", data)
    if data is None:
        raise HTTPException(status_code=500, detail="data summary can't be fetched")

    total=0
    for row in data:
        total+=row["total"]

    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']]={
        "total":row["total"],
        "percentage":round(percentage, 2)
    }
    print("DEBUG breakdown:", breakdown)
    return breakdown

@app.get("/analytics_by_month/")
def get_analytics():

    data2=db_helper.fetch_expense_summary_by_month()

    if data2 is None:
        raise HTTPException(status_code=500, detail="data2 summary can't be fetched")

    return data2






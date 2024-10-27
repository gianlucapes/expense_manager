from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from typing import List
from expense_model import Expense,DateRange

app= FastAPI()

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses=db_helper.fetch_expenses_for_date(expense_date=expense_date)
    return expenses


@app.post("/expenses/{expense_date}")
def get_expenses(expense_date: date,expenses:List[Expense]):
    for expense in expenses:
        db_helper.insert_expense(expense_date,expense.amount,expense.category,expense.notes)
    return {"message":"expenses are successful updated"}


@app.post("/analytics/category")
def get_analytics_by_category(date_range:DateRange):
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from database")
    
    total=sum([row['total'] for row in data])

    result={}

    for row in data:
        result[row['category']]={"total":row["total"],"percentage":(row['total']/total)*100 if total != 0 else 0}

    return result

@app.get("/analytics/month")
def get_analytics_by_category():
    data=db_helper.fetch_expense_grouped_by_month()
    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from database")
    return data
    
    
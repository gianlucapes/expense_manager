from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    amount : float
    category: str
    notes : str

class DateRange(BaseModel):
    start_date: date
    end_date:date


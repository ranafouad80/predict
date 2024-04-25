from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field, ValidationError
from fastapi.responses import JSONResponse
import pandas as pd
import joblib
from tabulate import tabulate

app = FastAPI()

# Load model and encoder
model = joblib.load("model.joblib")
encoder = joblib.load("encoder.joblib")
categorical_cols = ['الشعبة',"الوقت"]

# Define request body model
class PredictionRequest(BaseModel):
    الشعبة: str = Field(..., title="الشعبة")
    مدة_الدراسة: int = Field(..., title="مدة الدراسة")
    الاستراحه: float = Field(..., title="الاستراحه")
    الوقت: str = Field(..., title="الوقت")
    ضعيف_لغه_عربيه: int = Field(..., title="ضعيف لغه عربيه")
    ضعيف_لغه_انجليزيه: int = Field(..., title="ضعيف لغه انجليزيه")
    ضعيف_لغه_تانيه: int = Field(..., title="ضعيف لغه تانيه")
    ضعيف_كيمياء: int = Field(..., title="ضعيف  كيمياء")
    ضعيف_فيزياء: int = Field(..., title="ضعيف  فيزياء")
    ضعيف_احياء: int = Field(..., title="ضعيف احياء")
    ضعيف_جيولوجيا: int = Field(..., title="ضعيف جيولوجيا")
    ضعيف_رياضيات_باحتة: int = Field(..., title="ضعيف رياضيات باحتة")
    ضعيف_رياضيات_تطبيقيه: int = Field(..., title="ضعيف رياضيات تطبيقيه")
    ضعيف_علم_نفس_واجتماع: int = Field(..., title="ضعيف علم نفس واجتماع")
    ضعيف_تاريخ: int = Field(..., title="ضعيف تاريخ")
    ضعيف_جغرافيا: int = Field(..., title="ضعيف جغرافيا")
    ضعيف_فلسفة_ومنطق: int = Field(..., title="ضعيف فلسفة ومنطق")
    
# Function to print table for case 1
def print_case_one():
    data = [
        ["4.5:7.5","1:4","9.5:12.5","6:9"],
        ["فلسفةومنطق","لغه عربيه","جغرافيا","لغه انجليزيه"],
        ["لغه عربيه","لغه انجليزيه","تاريخ","علم نفس واجتماع"],
        ["تاريخ","فلسفةومنطق","جغرافيا","لغه عربيه"],
        ["فلسفةومنطق","لغه عربيه","لغه انجليزيه","تاريخ"],
        ["حل لغه عربيه","لغه انجليزيه","لغه تانيه","علم نفس واجتماع"],
        ["لغه انجليزيه","حل لغه تانيه","جغرافيا","حل علم نفس واجتماع"],
        ["حل جغرافيا","حل فلسفةومنطق","حل لغه انجليزيه","حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 2
def print_case_two():
    data = [
        ["11.5:2.5", "8:11", "4.5:7.5", "1:4"],
        ["فلسفة ومنطق", "لغه انجليزيه", "جغرافيا", "لغه عربيه"],
        ["لغه انجليزيه", "لغه عربيه", "تاريخ", "علم نفس واجتماع"],
        ["تاريخ", "فلسفة ومنطق", "جغرافيا", "لغه انجليزيه"],
        ["فلسفة ومنطق", "لغه انجليزيه", "لغه عربيه", "تاريخ"],
        ["حل لغه انجليزيه", "لغه عربيه", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه عربيه"],
        ["حل جغرافيا", "حل فلسفة ومنطق", "حل لغه عربيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 3
def print_case_three():
    data = [
        ["6:9", "2:5", "10:1", "6:9"],
        ["لغه تانيه", "لغه انجليزيه", "جغرافيا", "لغه عربيه"],
        ["لغه انجليزيه", "لغه عربيه", "تاريخ", "علم نفس واجتماع"],
        ["تاريخ", "فلسفة و منطق", "جغرافيا", "لغه انجليزيه"],
        ["فلسفة و منطق", "علم نفس اجتماع", "لغه عربيه", "تاريخ"],
        ["حل لغه انجليزيه", "لغه عربيه", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "تاريخ", "لغه عربيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه عربيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 4
def print_case_four():
    data = [
        ["1:4", "9:12", "5:8", "1:4"],
        ["فلسفة و منطق", "لغه عربيه", "جغرافيا", "لغه انجليزيه"],
        ["لغه عربيه", "لغه انجليزيه", "تاريخ", "علم نفس واجتماع"],
        ["تاريخ", "فلسفة و منطق", "جغرافيا", "لغه عربيه"],
        ["فلسفة و منطق", "لغه عربيه", "علم نفس واجتماع", "تاريخ"],
        ["حل لغه عربيه", "تاريخ", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه انجليزيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه انجليزيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 5
def print_case_five():
    data = [
        ["1.5:3.5", "11:1", "8.5:10.5", "6:8"],
        ["فلسفة و منطق", "لغه عربيه", "جغرافيا", "لغه انجليزيه"],
        ["لغه عربيه", "لغه انجليزيه", "تاريخ", "علم نفس واجتماع"],
        ["تاريخ", "فلسفة و منطق", "لغه تانيه", "لغه عربيه"],
        ["فلسفة و منطق", "لغه عربيه", "لغه انجليزيه", "تاريخ"],
        ["حل لغه عربيه", "لغه انجليزيه", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه انجليزيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه انجليزيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 6
def print_case_six():
    data = [
        ["8.5:10.5", "6:8", "3.5:5.5", "1:3"],
        ["فلسفة و منطق", "لغه عربيه", "جغرافيا", "لغه انجليزيه"],
        ["لغه عربيه", "لغه انجليزيه", "تاريخ", "علم نفس واجتماع"],
        ["تاريخ", "فلسفة و منطق", "علم نفس واجتماع", "لغه عربيه"],
        ["فلسفة و منطق", "لغه عربيه", "لغه انجليزيه", "تاريخ"],
        ["حل لغه عربيه", "لغه انجليزيه", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه انجليزيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه انجليزيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 7
def print_case_seven():
    data = [
        ["3:5", "12:2", "9:11", "6:8"],
        ["فلسفة و منطق", "لغه عربيه", "جغرافيا", "لغه انجليزيه"],
        ["لغه عربيه", "لغه انجليزيه", "لغه تانيه", "جغرافيا"],
        ["علم نفس واجتماع", "فلسفة و منطق", "جغرافيا", "لغه عربيه"],
        ["فلسفة و منطق", "لغه انجليزيه", "علم نفس واجتماع", "تاريخ"],
        ["حل لغه عربيه", "تاريخ", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه انجليزيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه انجليزيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 8
def print_case_eight():
    data = [
        ["10:12", "7:9", "4:6", "1:3"],
        ["تاريخ", "لغه عربيه", "فلسفه ومنطق", "لغه انجليزيه"],
        ["لغه عربيه", "لغه انجليزيه", "علم نفس واجتماع", "جغرافيا"],
        ["لغه تانيه", "فلسفة و منطق", "جغرافيا", "تاريخ"],
        ["فلسفة و منطق", "لغه انجليزيه", "علم نفس واجتماع", "لغه عربيه"],
        ["حل لغه عربيه", "تاريخ", "لغه تانيه", "علم نفس واجتماع"],
        ["حل علم نفس واجتماع", "حل لغه تانيه", "جغرافيا", "لغه انجليزيه"],
        ["حل جغرافيا", "حل فلسفة و منطق", "حل لغه انجليزيه", "حل تاريخ"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 9
def print_case_nine():
    data = [
        ["4.5:7.5", "1:4", "9.5:12.5", "6:9"],
        ["لغه انجليزيه", "لغه عربيه", "رياضيات باحته", "كيمياء"],
        ["لغه عربيه", "كيمياء", "رياضيات تطبيقيه", "فيزياء"],
        ["كيمياء", "لغه تانيه", "فيزياء", "لغه انجليزيه"],
        ["رياضيات باحته", "فيزياء", "علم رياضيات تطبيقيه", "لغه عربيه"],
        ["حل لغه عربيه", "لغه انجليزيه", "لغه تانيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "لغه انجليزيه", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 10
def print_case_ten():
    data = [
        ["11.5:2.5", "8:11", "4.5:7.5", "1:4"],
        ["لغه انجليزيه", "لغه عربيه", "رياضيات باحته", "كيمياء"],
        ["لغه عربيه", "كيمياء", "رياضيات تطبيقيه", "فيزياء"],
        ["كيمياء", "لغه تانيه", "فيزياء", "لغه انجليزيه"],
        ["رياضيات باحته", "فيزياء", "علم رياضيات تطبيقيه", "لغه عربيه"],
        ["حل لغه عربيه", "لغه انجليزيه", "فيزياء", "رياضيات باحته"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "لغه انجليزيه", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 11
def print_case_eleven():
    data = [
        ["6:9", "2:5", "10:1", "6:9"],
        ["فيزياء", "لغه انجليزيه", "رياضيات باحته", "كيمياء"],
        ["لغه عربيه", "كيمياء", "رياضيات تطبيقيه", "فيزياء"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه تانيه"],
        ["رياضيات باحته", "فيزياء", "علم رياضيات تطبيقيه", "لغه عربيه"],
        ["حل لغه عربيه", "لغه عربيه", "لغه انجليزيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "لغه انجليزيه", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 12
def print_case_twelve():
    data = [
        ["1:4", "9:12", "5:8", "1:4"],
        ["فيزياء", "لغه انجليزيه", "رياضيات باحته", "لغه عربيه"],
        ["لغه انجليزيه", "كيمياء", "رياضيات تطبيقيه", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["رياضيات باحته", "فيزياء", "علم رياضيات تطبيقيه", "لغه عربيه"],
        ["حل لغه عربيه", "لغه عربيه", "لغه تانيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "لغه انجليزيه", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 13
def print_case_thirteen():
    data = [
        ["1.5:3.5", "11:1", "8.5:10.5", "6:8"],
        ["فيزياء", "لغه انجليزيه", "رياضيات باحته", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["فيزياء", "كيمياء", "علم رياضيات تطبيقيه", "لغه انجليزيه"],
        ["حل لغه عربيه", "رياضيات باحته", "لغه انجليزيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 14
def print_case_fourteen():
    data = [
        ["8.5:10.5", "6:8", "3.5:5.5", "1:3"],
        ["فيزياء", "كيمياء", "رياضيات باحته", "لغه عربيه"],
        ["لغه انجليزيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["فيزياء", "كيمياء", "علم رياضيات تطبيقيه", "لغه انجليزيه"],
        ["حل لغه عربيه", "رياضيات باحته", "لغه انجليزيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 15
def print_case_fifteen():
    data = [
        ["3:5", "12:2", "9:11", "6:8"],
        ["فيزياء", "كيمياء", "رياضيات باحته", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["فيزياء", "لغه تانيه", "علم رياضيات تطبيقيه", "لغه انجليزيه"],
        ["حل لغه عربيه", "رياضيات باحته", "لغه انجليزيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 16
def print_case_sixteen():
    data = [
        ["10:12", "7:9", "4:6", "1:3"],
        ["فيزياء", "لغه انجليزيه", "رياضيات باحته", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "رياضيات تطبيقيه"],
        ["كيمياء", "لغه انجليزيه", "رياضيات باحته", "لغه عربيه"],
        ["فيزياء", "لغه تانيه", "علم رياضيات تطبيقيه", "لغه انجليزيه"],
        ["حل لغه عربيه", "رياضيات باحته", "لغه انجليزيه", "رياضيات تطبيقيه"],
        ["حل رياضيات تطبيقيه", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل رياضيات باحته", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 17
def print_case_seventeen():
    data = [
        ["4.5:7.5", "1:4", "9.5:12.5", "6:9"],
        ["لغه انجليزيه", "كيمياء", "احياء", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["فيزياء", "كيمياء", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه تانيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 18
def print_case_eighteen():
    data = [
        ["11.5:2.5", "8:11", "4.5:7.5", "1:4"],
        ["فيزياء", "كيمياء", "احياء", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["فيزياء", "كيمياء", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه انجليزيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 19
def print_case_nineteen():
    data = [
        ["6:9", "2:5", "10:01", "6:9"],
        ["فيزياء", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "لغه انجليزيه", "فيزياء", "لغه عربيه"],
        ["لغه عربيه", "كيمياء", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه انجليزيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "لغه انجليزيه"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 20
def print_case_twenty():
    data = [
        ["1:4", "9:12", "5:8", "1:4"],
        ["لغه تانيه", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["احياء", "فيزياء", "كيمياء", "لغه تانيه"],
        ["كيمياء", "جيولوجيا", "فيزياء", "لغه عربيه"],
        ["لغه عربيه", "كيمياء", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه انجليزيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "لغه انجليزيه"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
 # Function to print table for case 21
def print_case_twenty_one():
    data = [
        ["1.5:3.5", "11:1", "8.5:10.5", "6:8"],
        ["لغه انجليزيه", "احياء", "فيزياء", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "جيولوجيا"],
        ["كيمياء", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["فيزياء", "كيمياء", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه تانيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 22
def print_case_twenty_two():
    data = [
        ["8.5:10.5", "6:8", "3.5:5.5", "1:3"],
        ["كيمياء", "احياء", "فيزياء", "لغه تانيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه انجليزيه"],
        ["كيمياء", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["فيزياء", "لغه عربيه", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه تانيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 23
def print_case_twenty_three():
    data = [
        ["3:5", "12:2", "9:11", "6:8"],
        ["لغه تانيه", "احياء", "فيزياء", "لغه عربيه"],
        ["لغه عربيه", "فيزياء", "كيمياء", "لغه انجليزيه"],
        ["كيمياء", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["فيزياء", "لغه عربيه", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه تانيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")
# Function to print table for case 24
def print_case_twenty_four():
    data = [
        ["10:12", "7:9", "4:6", "1:3"],
        ["لغه تانيه", "احياء", "فيزياء", "لغه عربيه"],
        ["لغه انجليزيه", "فيزياء", "كيمياء", "لغه انجليزيه"],
        ["كيمياء", "لغه انجليزيه", "احياء", "لغه عربيه"],
        ["فيزياء", "لغه عربيه", "جيولوجيا", "لغه انجليزيه"],
        ["حل لغه عربيه", "احياء", "لغه تانيه", "جيولوجيا"],
        ["حل احياء", "حل لغه تانيه", "فيزياء", "كيمياء"],
        ["حل فيزياء", "حل جيولوجيا", "حل لغه انجليزيه", "حل كيمياء"]
    ]
    headers = data[0]  # Use the first row as headers
    data = data[1:]    # Remove the first row from the data
    return tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center")


# Define prediction route
@app.post("/predict/")
async def predict(data: PredictionRequest):
    try:
        data_dict = data.dict()
        new_key_mapping = {key: key.replace('_', ' ') for key, value in data_dict.items()}
        new_key_mapping['ضعيف_فيزياء']= 'ضعيف  فيزياء'
        new_key_mapping['ضعيف_كيمياء']= 'ضعيف  كيمياء'
    # print(data_dict.items())

        updated_dict = {new_key_mapping.get(k): v for k, v in data_dict.items()}
        df = pd.DataFrame([updated_dict])
        # One-hot encode the new data using the saved encoder
        one_hot_encoded_new_data = encoder.transform(df[categorical_cols])
        one_hot_encoded_df = pd.DataFrame(one_hot_encoded_new_data, columns=encoder.get_feature_names_out())
        df = pd.concat([df.drop(columns=categorical_cols), one_hot_encoded_df], axis=1)

        # Make predictions on the new data using the saved model
        new_predictions = model.predict(df)

        # Output table based on prediction
        # Define a dictionary to map predictions to functions
        switch_cases = {
        1: print_case_one,
        2: print_case_two,
        3: print_case_three,
        4: print_case_four,
        5: print_case_five,
        6: print_case_six,
        7: print_case_seven,
        8: print_case_eight,
        9: print_case_nine,
        10: print_case_ten,
        11: print_case_eleven,
        12: print_case_twelve,
        13: print_case_thirteen,
        14: print_case_fourteen,
        15: print_case_fifteen,
        16: print_case_sixteen,
        17: print_case_seventeen,
        18: print_case_eighteen,
        19: print_case_nineteen,
        20: print_case_twenty,
        21: print_case_twenty_one,
        22: print_case_twenty_two,
        23: print_case_twenty_three,
        24: print_case_twenty_four
        }


        table = switch_cases.get(new_predictions[0], lambda: "No corresponding case")()

        return Response(content=table, media_type="text/plain")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

# Error handler for validation errors
@app.exception_handler(422)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={"error": "Validation Error", "details": exc.errors()})

# Error handler for general exceptions
@app.exception_handler(500)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"error": "Internal Server Error"})

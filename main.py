from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field, ValidationError
from fastapi.responses import JSONResponse
import pandas as pd
import joblib

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

        # Output prediction
        return {"predictions": new_predictions.tolist()}
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

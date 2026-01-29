from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict_output import predict_output,model,MODEL_VERSION

app = FastAPI()
      
@app.get('/')
def home():
    return "Insurnace Premium Prediction API"

@app.get('/health')
def health_check():
    return {
        'Status':'Ok',
        'Version':MODEL_VERSION,
        'Model loaded' : model is not None
    }
    
@app.post("/predict")
def predict(data: UserInput):
    user_input = {
        'bmi' : data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    prediction = predict_output(user_input)
    return JSONResponse(status_code=200,content={'Predicted_category': prediction})
    
    
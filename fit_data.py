import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib

def train_and_save_model(excel_file, model_file, encoder_file):
    # Load data from Excel file
    df = pd.read_excel(excel_file)

    # Preprocessing (handle missing values, one-hot encode categorical variables, etc.)
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object']
    one_hot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    one_hot_encoded = one_hot_encoder.fit_transform(df[categorical_cols])

    # Save encoder for new data
    joblib.dump(one_hot_encoder, encoder_file)

    one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_cols))
    df = pd.concat([df.drop(columns=categorical_cols), one_hot_encoded_df], axis=1)

    # Split features and target variable
    X = df.drop(columns=["تصنيف"])
    y = df["تصنيف"]

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    # Save model
    joblib.dump(model, model_file)

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    excel_file = "the final data.xlsx"
    model_file = "model.joblib"
    encoder_file = "encoder.joblib"
    train_and_save_model(excel_file, model_file, encoder_file)

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def preprocess_data(df, categorical_cols):
    # Handle missing values if any (e.g., fill with mode or drop)
    df = df.dropna()
    
    # One-hot encode categorical variables
    one_hot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    one_hot_encoded = one_hot_encoder.fit_transform(df[categorical_cols])
    
    # Create a DataFrame with one-hot encoded columns
    one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_cols))
    
    # Drop original categorical columns and concatenate one-hot encoded columns
    df = pd.concat([df.drop(columns=categorical_cols), one_hot_encoded_df], axis=1)
    
    return df, one_hot_encoder

def train_and_save_model(excel_file, model_file, encoder_file):
    # Load data from Excel file
    df = pd.read_excel(excel_file)

    # Define categorical columns
    categorical_cols = ['الشعبة', 'الوقت']
    
    # Preprocess the data
    df, one_hot_encoder = preprocess_data(df, categorical_cols)
    
    # Save the encoder for future use
    joblib.dump(one_hot_encoder, encoder_file)
    
    # Split data into features (X) and target variable (y)
    X = df.drop(columns=["تصنيف"])
    y = df["تصنيف"]
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Train the RandomForest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, model_file)
    
    # Make predictions on the testing set
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
    
if __name__ == "__main__":
    excel_file = "the final data.xlsx"
    model_file = "model.joblib"
    encoder_file = "encoder.joblib"
    train_and_save_model(excel_file, model_file, encoder_file)

# Main Entrypoint
from parameters.parameters import (
    file_path, autogluon_params
)
from data_ingestion.ingest import get_data
from model_building.build_model import autogluon_model_build
import time

# Stage 0 - Data Ingestion
print("Starting Data Ingestion")
print("Starting Authors Data...")
start_time = time.time()
author_data_new = get_data(file_path)
end_time = time.time()
print(f"Execution time for Author Data Ingestion is {end_time - start_time} seconds")
#print(f"Size of Author Data is {author_data_new.shape}")
print(author_data_new.head())

# Stage 1 - Model Building
print("Starting Model Builidng...")
start_time = time.time()
train_data, test_data, predictor = (
    autogluon_model_build(author_data_new, autogluon_params)
)
end_time = time.time()
print(f"Execution time for Model Building is {end_time - start_time} seconds")
print(f"Size of Train Data is {train_data.shape}")
print(f"Size of Test Data is {test_data.shape}")

# Stage 2 - Model Evaluation
print("Starting Model Evaluation...")
start_time = time.time()
print(predictor.leaderboard(silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Train) is {end_time - start_time} seconds")
start_time = time.time()
print(predictor.leaderboard(test_data, silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Test) is {end_time - start_time} seconds")
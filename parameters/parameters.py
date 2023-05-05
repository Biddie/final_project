import os

FILE_NAME = "author_data_new.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)

autogluon_params = {
    "save_path": 'artefacts/models_author_regression',
    "time_limit": 60,
    "label": "sentiment"
    #"problem_type": "sentiment"
} 
import os

AUTHORS_FILE_NAME = "Author_data.csv"

DATA_FOLDER = "data"
main_path = os.getcwd()

author_file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), AUTHORS_FILE_NAME)

autogluon_params = {
    "save_path": 'artefacts/models_author_regression',
    "time_limit": 60,
    "label": "sentiment"
}
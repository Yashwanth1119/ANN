import os
from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model, save_model
import argparse

def training(config_path):
    history = model.fit(X_train, y_train, epochs=EPOCHS,
                    validation_data=VALIDATION_SET)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model_dir"]

    model_dir_path = os.path.join(artifacts_dir, model_dir)
    os.makedirs(model_dir_path, exist_ok=True)

    model_name = config["artifacts"]["model_name"]

    save_model(model, model_name, model_dir_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
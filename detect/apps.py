from django.apps import AppConfig
import pickle
from tensorflow.keras.models import model_from_json
class DetectConfig(AppConfig):
    name = 'detect'
    mdl=pickle.load(open('assets/cancer1.sav','rb'))
    json_file = open('assets/cnn.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("assets/cnn.h5")
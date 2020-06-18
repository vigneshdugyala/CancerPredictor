from django.apps import AppConfig
import pickle
#import xgboost
class DetectConfig(AppConfig):
    name = 'detect'
    mdl=pickle.load(open('assets/cancer1.sav','rb'))

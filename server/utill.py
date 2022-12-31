import pickle
import json


__emotions = None
__model = None
__v = None

def prediction(text):
    global __model
    global __emotions
    global __v
    text_count = __v.transform([text])

    return __emotions[__model.predict(text_count)[0]]

def get_emotionss():
    global __emotions
    return __emotions

def load_saved_model():
    global __emotions
    global __model
    global __v

    with open("./model/Emotions.json", 'r') as f:
        __emotions = json.load(f)['Emotions']

    with open("./model/emotion_classification2.pickle", 'rb') as f:
        __v,__model = pickle.load(f)
        print('model was loaded')

if __name__ == "__main__":
    '''sentances = [
        'I am so sad from the service',
        'I am happy to be one of the solider to serve my country in this global crisis',
        'i am tired',
        'i was shocked  to hear that',
        'it would be a pleasure to cooperate with you'
    ]'''
    load_saved_model()
    print(get_emotionss())
    print(prediction('it would be a pleasure to cooperate with you'))
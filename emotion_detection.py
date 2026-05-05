import requests
import json

def emotion_detector(text_to_analyze):
    """
        Emotion Predict function of the Watson NLP Library
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)

    response_json = json.loads(response.text)
    emotions_dict = response_json['emotionPredictions'][0]['emotion']

    # dominant emotion
    dominant_emotion = None
    dominant_score = 0

    for emotion in list(emotions_dict.keys()):
        if emotions_dict[emotion] >= dominant_score:
            dominant_emotion = emotion
            dominant_score = emotions_dict[emotion]
    
    emotions_dict["dominant_emotion"] = dominant_emotion

    return emotions_dict
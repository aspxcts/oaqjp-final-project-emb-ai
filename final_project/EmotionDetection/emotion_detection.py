import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)

        if response.status_code == 200:
            response_json = response.json()
            emotions = response_json["emotionPredictions"][0]["emotion"]
            
            anger_score = emotions.get('anger', None)
            disgust_score = emotions.get('disgust', None)
            fear_score = emotions.get('fear', None)
            joy_score = emotions.get('joy', None)
            sadness_score = emotions.get('sadness', None)
            
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Construct the formatted output dictionary
            output = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            
            return output
        elif response.status_code == 400:
            # Handle blank entry error
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            print(f"Error: Emotion Detection request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: An exception occurred - {e}")
        return None
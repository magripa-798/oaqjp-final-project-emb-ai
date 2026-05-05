''' Executing this function initiates the application of emotiom
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request
from flask import Flask, render_template, request
# Import the emotion_detector
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions with respective
        and dominant emotion for the provided text.
    '''

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again"
    text_to_return = "For the given statement," + \
                     f"the system response is 'anger': {str(response['anger'])}, " + \
                     f"'disgust': {str(response['disgust'])}, 'fear': {str(response['fear'])}, " + \
                     f"'joy': {str(response['joy'])}," + \
                     f" and 'sadness': {str(response['sadness'])}." + \
                     f"The dominant emotion is {str(response['dominant_emotion'])}."

    return text_to_return

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

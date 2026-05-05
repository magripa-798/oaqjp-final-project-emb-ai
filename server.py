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
    
    text_to_return = "For the given statement, the system response is 'anger': {}, ".format(str(response['anger'])) + \
                       "'disgust': {}, 'fear': {}, ".format(str(response['disgust']), str(response['fear'])) + \
                       "'joy': {}, and 'sadness': {}.".format(str(response['joy']), str(response['sadness'])) + \
                       "The dominant emotion is {}.".format(str(response['dominant_emotion']))

    return text_to_return

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
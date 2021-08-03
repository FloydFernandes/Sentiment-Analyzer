from flask import Flask, render_template, request
import analysis


app = Flask(__name__)


def single_none():
    single_sentiment_null = {"Negative": 0, "Neutral": 0, "Positive": 0}
    single_emotion_null = {"Happy": 0, "Angry": 0, "Sad": 0, "Surprise": 0, "Fear": 0}

    return [single_sentiment_null, single_emotion_null]


@app.route('/')
def home():
    single_none_data = single_none() 
    single_sentiment_null = single_none_data[0]

    single_emotion_null = single_none_data[1]

    return render_template("single_user.html", sentiment = single_sentiment_null,
            emotion = single_emotion_null)


@app.route('/features_single', methods=['GET', 'POST'])
def single_user_features():

    single_none_data = single_none() 
    single_sentiment_null = single_none_data[0]

    single_emotion_null = single_none_data[1]

    if request.method == "POST":
        if request.form["user-text"] == "":

            render_template("single_user.html", sentiment = single_sentiment_null,
            emotion = single_emotion_null)

        else:    
            text = request.form["user-text"]
            
            sentiment_data = analysis.single_sentiment_analyzer(text)

            single_sentiment = {}

            for k, v in sentiment_data.items():
                if k != "compound":
                    if k == "neg":
                        single_sentiment["Negative"] = v
                    elif k == "neu":
                        single_sentiment["Neutral"] = v
                    else:
                        single_sentiment["Positive"] = v

            single_emotion = analysis.single_emotion_analyzer(text)

            return render_template("single_user.html", sentiment = single_sentiment,
            emotion = single_emotion, text=text)

    return render_template("single_user.html", sentiment = single_sentiment_null,
    emotion = single_emotion_null)


@app.route('/about')
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True , port=8000)
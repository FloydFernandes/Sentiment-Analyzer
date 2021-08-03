from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as te

def single_sentiment_analyzer(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)

    return score

def single_emotion_analyzer(text):
    emot = te.get_emotion(text)

    return emot
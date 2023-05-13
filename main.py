import requests
from nltk.sentiment import SentimentIntensityAnalyzer
from send_mail import send_mail

analyzer = SentimentIntensityAnalyzer()
key = ""

url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={key}"

request = requests.get(url)
content = request.json()

# Analyzer title. Get score
for article in content['articles']:
    scores = analyzer.polarity_scores(article['title'])
    article['score'] = dict(scores)

# Create positive news
positive_news = []

for pos_news in content['articles']:
    if pos_news['score']['pos'] > pos_news['score']['neg']:
        positive_news.append(pos_news)
    else:
        continue

message = ""
for news in positive_news[:20]:
    if news["title"] is not None:
        message = "Subject: Today News" \
                  + "\n" + message + news['title']\
                  + "\n" + news['description']\
                  +'\n' + news['url'] + 2*'\n'

send_mail(message=message)





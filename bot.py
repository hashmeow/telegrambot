from flask import Flask
import slack
import os
from dotenv import load_dotenv, find_dotenv
from slackeventsapi import SlackEventAdapter

load_dotenv(find_dotenv())
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

slack_token = os.getenv('SLACK_TOKEN')
client = slack.WebClient(token=slack_token)

client.chat_postMessage(channel='#bots', text='Hello world!')
BOT_ID = client.api_call("auth.test")["user_id"]


@slack_events_adapter.on("message")
def handle_message(event_data):
    event = event_data.get("event", {})
    channel = event.get("channel")
    user_id = event.get("user")
    if BOT_ID != user_id:
        text = event.get("text")

@app.route('/me ')
def me_made_messages(event_data):
    event = event_data.get("event", {})
    channel = event.get("me")
    user_id = event.get("user")
    if BOT_ID != user_id:
        text = event.get("text")



if __name__ == '__main__':
    app.run(debug=True)
    

import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
import graphviz
from utils import send_text_message_reply

load_dotenv()


machine = TocMachine(
    states=["user", "start", "tired","sad","worried","angry","stressed","movement","hydrate","positive_statement","gratitude_meditation","worry_time","guided_imagery","muscle_relaxation","grounded_meditation","cleaning_up","counting_backward","end"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start", 
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "tired",
            "conditions": "is_tired",
        },
        {
            "trigger": "advance",
            "source": "tired",
            "dest": "movement",
            "conditions": "is_movement",
        },
        {
            "trigger": "advance",
            "source": "tired",
            "dest": "hydrate",
            "conditions": "is_hydrate",
        },
        {
            "trigger": "advance",
            "source": "movement",
            "dest": "hydrate",
            "conditions": "is_yes_tired",
        },
        {
            "trigger": "advance",
            "source": "hydrate",
            "dest": "movement",
            "conditions": "is_yes_tired",
        },
        {
            "trigger": "advance",
            "source": ["hydrate","movement"],
            "dest": "end",
            "conditions": "is_no_tired",
        },

         {
            "trigger": "advance",
            "source": "start",
            "dest": "sad",
            "conditions": "is_sad",
        },
        {
            "trigger": "advance",
            "source": "sad",
            "dest": "positive_statement",
            "conditions": "is_positive_statement",
        },
        {
            "trigger": "advance",
            "source": "sad",
            "dest": "gratitude_meditation",
            "conditions": "is_gratitude_meditation",
        },
        {
            "trigger": "advance",
            "source": "positive_statement",
            "dest": "gratitude_meditation",
            "conditions": "is_yes_sad",
        },
        {
            "trigger": "advance",
            "source": "gratitude_meditation",
            "dest": "positive_statement",
            "conditions": "is_yes_sad",
        },
        {
            "trigger": "advance",
            "source":["positive_statement","gratitude_meditation"],
            "dest": "end",
            "conditions": "is_no_sad",
        },

        {
            "trigger": "advance",
            "source": "start",
            "dest": "worried",
            "conditions": "is_worried",
        },
        {
            "trigger": "advance",
            "source": "worried",
            "dest": "worry_time",
            "conditions": "is_worry_time",
        },
        {
            "trigger": "advance",
            "source": "worried",
            "dest": "guided_imagery",
            "conditions": "is_guided_imagery",
        },
        {
            "trigger": "advance",
            "source": "worry_time",
            "dest": "guided_imagery",
            "conditions": "is_yes_worried",
        },
        {
            "trigger": "advance",
            "source": "guided_imagery",
            "dest": "worry_time",
            "conditions": "is_yes_worried",
        },
        {
            "trigger": "advance",
            "source": ["worry_time","guided_imagery"],
            "dest": "end",
            "conditions": "is_no_worried",
        },

        {
            "trigger": "advance",
            "source": "start",
            "dest": "stressed",
            "conditions": "is_stressed",
        },
        {
            "trigger": "advance",
            "source": "stressed",
            "dest": "muscle_relaxation",
            "conditions": "is_muscle_relaxation",
        },
        {
            "trigger": "advance",
            "source": "stressed",
            "dest": "grounded_meditation",
            "conditions": "is_grounded_meditation",
        },
        {
            "trigger": "advance",
            "source": "muscle_relaxation",
            "dest": "grounded_meditation",
            "conditions": "is_yes_stressed",
        },
        {
            "trigger": "advance",
            "source": "grounded_meditation",
            "dest": "muscle_relaxation",
            "conditions": "is_yes_stressed",
        },
        {
            "trigger": "advance",
            "source": ["muscle_relaxation","grounded_meditation"],
            "dest": "end",
            "conditions": "is_no_stressed",
        },

        {
            "trigger": "advance",
            "source": "start",
            "dest": "angry",
            "conditions": "is_angry",
        },
        {
            "trigger": "advance",
            "source": "angry",
            "dest": "cleaning_up",
            "conditions": "is_cleaning_up",
        },
        {
            "trigger": "advance",
            "source": "angry",
            "dest": "counting_backward",
            "conditions": "is_counting_backward",
        },
        {
            "trigger": "advance",
            "source": "cleaning_up",
            "dest": "counting_backward",
            "conditions": "is_yes_angry",
        },
        {
            "trigger": "advance",
            "source": "counting_backward",
            "dest": "cleaning_up",
            "conditions": "is_yes_angry",
        },
        {
            "trigger": "advance",
            "source": ["cleaning_up","counting_backward"],
            "dest": "end",
            "conditions": "is_no_angry",
        },
        {
            "trigger": "advance",
            "source": "end",
            "dest": "start",
            "conditions": "is_going_to_start",
        }


    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue

        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")

        response = machine.advance(event)
        if response == False:
            reply_token = event.reply_token
            send_text_message_reply(reply_token,"Mochi is just a cat, I don't understand human language that well, please repeat it~")
            machine.get_graph().draw("fsm.png", prog="dot", format="png")

        return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)

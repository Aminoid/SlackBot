import os
import time
from slackclient import SlackClient

BOT_ID = os.environ.get("BOT_ID")

AT_BOT = "<@" + BOT_ID + ">"
COMMAND = "do"

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'));

def handle_command(command, channel):

    response = "Not sure what you mean. Use the *" + COMMAND + \
               "* command"
    if command.startswith(COMMAND):
        response = "Sure...write some code first dumbass!!!!!"

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    SOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print ("bt-7274 is running bitches!!!!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(SOCKET_DELAY)
    else:
        print ("Connection failed. Fix it Kaake!!!")


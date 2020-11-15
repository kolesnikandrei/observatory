from slack import WebClient
SLACK_TOKEN = "xoxb-1286293502836-1483429389328-ylb8HimTPvqm0lP1RSYBPP3d"

slack_client = WebClient(token=SLACK_TOKEN)


bot_id = slack_client.api_call('auth.test')['user_id']
print(bot_id)

slack_client.chat_postMessage(channel='tst', text='Hello World!')
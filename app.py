from flask import Flask, render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

app= Flask(__name__)

with open('chat.txt',"r") as file:
    conversation = file.read()

bot = ChatBot("Global Voice Chatbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

bot = ChatBot(
    'Global Voice Chatbot',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance.',
'Sure, how can i help you?',
'Can you show me the map of America?',
'Sure, here you can see the map of America, would you like to see a country in specific?',
'Can you show me Panama City?',
'Sure, Panama City Florida or Panama City Panama?',
'Panama City Panama',
"Wonderful, here you go with Panama's location in the map.",
'Can you show me United States now?',
'Yes, sure there you go.',
'Can you show me Brazil now?',
'Yes, sure there you go.',
'Can you show me Mexico now?',
'Yes, sure there you go.',
'Can you show me Colombia now?',
'Yes, sure there you go.',
'Can you show me Argentina now?',
'Yes, sure there you go.',
'Can you show me Canada now?',
'Yes, sure there you go.',
'Can you show me Peru now?',
'Yes, sure there you go.',
'Can you show me Venezuela now?',
'Yes, sure there you go.',
'Can you show me Chile now?',
'Yes, sure there you go.',
'Can you show me Ecuador now?',
'Yes, sure there you go.',
'Can you show me Guatemala now?',
'Yes, sure there you go.',
'Can you show me Cuba now?',
'Yes, sure there you go.',
'Can you show me Bolivia now?',
'Yes, sure there you go.',
'Can you show me Haiti now?',
'Yes, sure there you go.',
'Can you show me Dominican Republic now?',
'Yes, sure there you go.',
'Can you show me Honduras now?',
'Yes, sure there you go.',
'Can you show me Paraguay now?',
'Yes, sure there you go.',
'Can you show me Nicaragua now?',
'Yes, sure there you go.',
'Can you show me El Salvador now?',
'Yes, sure there you go.',
'Can you show me Costa Rica now?',
'Yes, sure there you go.',
'Can you show me Puerto Rico now?',
'Yes, sure there you go.',
'Can you show me Uruguay now?',
'Yes, sure there you go.',
'Can you show me Jamaica now?',
'Yes, sure there you go.',
'Can you show me Trinidad and Tobago now?',
'Yes, sure there you go.',
'Can you show me Guyana now?',
'Yes, sure there you go.',
'Can you show me Suriname now?',
'Yes, sure there you go.'
])


@app.route("/app")
def chat():
    return render_template("chat.html")

@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    return str(bot.get_response(usertext))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resources")
def resources():
    return render_template("resources.html") 

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(debug=True)
import warnings
warnings.filterwarnings("ignore")
import os
from flask import Flask,request,jsonify
from uploadpdf import vector
from askquestion import ask_question

app = Flask(__name__)

@app.route('/question', methods=["POST"])
def question():
    uuid = request.json['uuid']
    query = request.json['query']
    answer=ask_question(str(uuid),str(query))
    print(answer)
    return jsonify(answer)


@app.route('/uploadpdf', methods=["POST"])
def uploadpdf():
    pdf = request.json['pdf']
    uuid = request.json['uuid']
    persist_directory=vector(str(uuid),str(pdf))
    print(persist_directory)
    return jsonify(persist_directory)



if __name__ == '__main__':
	app.run()

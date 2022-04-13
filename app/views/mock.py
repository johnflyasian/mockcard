
from flask import Blueprint, jsonify, Response
import random

mockresponse = Blueprint('mockresponse', __name__)
RANKCLASS = ('2','3','4','5', "6", "7", "8", "9", "10", "J", "Q", "K", "A")
SUITCLASS = ('diamond', 'club','heart','spade')

@mockresponse.route("/getcards", methods=["GET"])
def getcards():
    return jsonify(random_cards())


def random_cards():
    random_number_of_cards = 6 #random.randint(0,6)
    output = []
    for i in range(random_number_of_cards):
        output.append( {"cardno":i+1, "rank": random.choice(RANKCLASS), "suit": random.choice(SUITCLASS)} )
    return {"cards":output}
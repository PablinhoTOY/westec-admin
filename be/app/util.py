import os.path as path
from flask import request, jsonify
from datetime import datetime
from app.Models.Users import User


def generateResponse(title, message):
    return jsonify({
            "title": title,
            "status": "200",
            "mensaje": message
        }),200


def generateError(title, code, message):
    return jsonify({   
            "title": title,
            "status": code,
            "mensaje": message
        }),code


# helper functions for authentication£
def userIsAdmin (user_id):
    user = User.query.filter_by(id=user_id).first()
    if (user):
        for role in user.roles:
            if role.name == 'admin':
                return True
        return False
    else:
        return False


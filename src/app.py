from flask import Flask, jsonify, request
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.route("/members", methods=["GET"])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Invalid data"}), 400

    try:
        jackson_family.add_member(data)
        return jsonify(data), 200  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    try:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
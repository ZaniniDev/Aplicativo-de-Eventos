from flask import Blueprint, jsonify, render_template, request
from src.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_error

front_end_app_route_bp = Blueprint("front_app_routes", __name__)

@front_end_app_route_bp.route("/createEvent", methods=["GET"])
def create_event():
    return render_template("create_event.html")

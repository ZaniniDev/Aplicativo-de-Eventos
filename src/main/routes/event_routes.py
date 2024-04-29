import uuid
from flask import Blueprint, jsonify, request, session
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler
from src.errors.error_handler import handle_error
from src.models.repository.users_repository import UsersRepository

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    
    if 'session_uuid' not in session:
        session['session_uuid'] = str(uuid.uuid4())
        user_agent = request.headers.get('User-Agent')
        remote_addr = request.remote_addr        
        user_repository = UsersRepository()
        infos_user = {"uuid": session['session_uuid'], "name": "Visitante", "email": session['session_uuid']+"@"+remote_addr+"@"+user_agent}
        user_repository.insert_user(infos_user)      
        
    body=request.json
    
    #Validação temporaria de usuario 
    user_id = session['session_uuid']   
    body["user_id"] = user_id
    
    try:
        http_request = HttpRequest(body=request.json)
        event_handler = EventHandler()
        http_response = event_handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    try:
        event_handler = EventHandler()
        http_request = HttpRequest(param={ "event_id": event_id })

        http_response = event_handler.find_by_id(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@event_route_bp.route("/activesEvents", methods=["GET"])
def get_actives_events():
    
    if 'session_uuid' not in session:
        session['session_uuid'] = str(uuid.uuid4())
        user_agent = request.headers.get('User-Agent')
        remote_addr = request.remote_addr        
        user_repository = UsersRepository()
        infos_user = {"uuid": session['session_uuid'], "name": "Visitante", "email": session['session_uuid']+"@"+remote_addr+"@"+user_agent}
        user_repository.insert_user(infos_user)     
         
    try:
        event_handler = EventHandler()
        http_request = HttpRequest()
        http_response = event_handler.find_events_actives(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

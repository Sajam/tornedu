from core.web import RequestHandler
from .auth import Auth


RequestHandler.get_current_user = Auth.get_current_user
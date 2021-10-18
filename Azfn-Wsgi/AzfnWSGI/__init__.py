import azure.functions as func  
from .app import application

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(application.wsgi_app).handle(req, context)

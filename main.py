from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request
from billetto_api import soeg_events, hent_event
import os

async def soeg_events_endpoint(request: Request):
    """Endpoint for at søge efter Billetto events."""
    limit = request.query_params.get('limit', 10)
    postal_code = request.query_params.get('postal_code')
    macroregion = request.query_params.get('macroregion')
    region = request.query_params.get('region')
    subregion = request.query_params.get('subregion')
    organizer_id = request.query_params.get('organizer_id')
    type = request.query_params.get('type')
    category = request.query_params.get('category')
    subcategory = request.query_params.get('subcategory')

    result = soeg_events(
        limit=int(limit),
        postal_code=postal_code,
        macroregion=macroregion,
        region=region,
        subregion=subregion,
        organizer_id=organizer_id,
        type=type,
        category=category,
        subcategory=subcategory
    )
    return JSONResponse(result)

async def hent_event_endpoint(request: Request, event_id: str):
    """Endpoint for at hente et specifikt Billetto event."""
    result = hent_event(event_id=event_id)
    return JSONResponse(result)

routes = [
    Route("/billetto/events", soeg_events_endpoint, methods=["GET"]),
    Route("/billetto/events/{event_id}", hent_event_endpoint, methods=["GET"]),
]

app = Starlette(routes=routes)

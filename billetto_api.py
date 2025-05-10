import requests
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://billetto.dk/api/v3/public"

def soeg_events(limit: int = 10, postal_code: str = None, macroregion: str = None,
                region: str = None, subregion: str = None, organizer_id: str = None,
                type: str = None, category: str = None, subcategory: str = None):
    """Søger efter offentlige events på Billetto."""
    url = f"{BASE_URL}/events"
    params = {
        "limit": limit,
        "postal_code": postal_code,
        "macroregion": macroregion,
        "region": region,
        "subregion": subregion,
        "organizer_id": organizer_id,
        "type": type,
        "category": category,
        "subcategory": subcategory
    }
    params = {k: v for k, v in params.items() if v is not None}
    headers = {"accept": "application/json"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Fejl ved kald til Billetto API: {e}")
        return {"error": f"Fejl ved hentning af data fra Billetto API: {e}"}

def hent_event(event_id: str):
    """Henter detaljer for et specifikt event fra Billetto."""
    url = f"{BASE_URL}/events/{event_id}"
    headers = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Fejl ved hentning af event {event_id} fra Billetto API: {e}")
        return {"error": f"Fejl ved hentning af eventdetaljer: {e}"}

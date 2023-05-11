import logging
from typing import Any, Dict, List, cast

import requests
from decouple import config  # type: ignore
from cirrus_sdk import CirrusClient

import json

logger = logging.getLogger(__name__)


context = json.dumps(
    {
        "app_id": "fenix",
        "app_name": "fenix",
        "channel": "developer",
    }
)
client = CirrusClient(context)


class RemoteSettings:
    recipes: List[Dict[str, Any]] = {"data": []}
    url: str = cast(str, config("REMOTE_SETTING_URL", default=""))

    @classmethod
    def get_recipes(cls) -> List[Dict[str, Any]]:
        return cls.recipes

    def update_recipes(self, new_recipes: List[Dict[str, Any]]) -> None:
        self.recipes = new_recipes
        client.set_experiments(json.dumps(self.recipes))

    def fetch_recipes(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json().get("data", [])
                if data:
                    self.update_recipes({"data": data})
                    logger.info("Fetched resources")
                else:
                    logger.warning("No recipes found in the response")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch recipes: {e}")
            raise e

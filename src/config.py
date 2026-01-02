import json
from pathlib import Path


class ConfigLoader:
    def __init__(self, config_path: str = "config/config.json"):
        self.config_path = Path(config_path)
        self._config = self._load()

    def _load(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        with open(self.config_path, "r") as f:
            return json.load(f)

    def get_waf_config(self):
        return self._config.get("waf", {})

    def get_logging_config(self):
        return self._config.get("logging", {})

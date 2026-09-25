from pathlib import Path
import tomllib


def load_config():
    config_path = Path("contractguard.toml")

    if not config_path.exists():
        raise FileNotFoundError(
            "contractguard.toml not found !"
            "Run `contractguard init` from your FastAPI project."
        )

    with open(config_path,"rb") as file:
        config = tomllib.load(file)
        
    return config
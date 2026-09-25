import importlib

def load_fastapi_app(app_path:str):

    if ":" not in app_path:
        raise ValueError(
            "Invalid app path. Use the format `module:app`, "
            "for eg. `main:app` "
        )
    module_name,app_name = app_path.split(":",1)

    module = importlib.import_module(module_name)
    print("MAIN MODULE LOADED FROM:", module.__file__)
    app = getattr(module,app_name)
    print("Returning app value : (load_fast_api) function : ",app)
    return app

def generate_openapi(app_path:str):
    app = load_fastapi_app(app_path=app_path)

    return app.openapi()
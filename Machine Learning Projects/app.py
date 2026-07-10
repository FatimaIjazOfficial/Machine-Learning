import os
from flask import Flask
from flask_cors import CORS
from config import Config
from routes.documents import documents_bp
from routes.home import home_bp
from routes.query import query_bp
from routes.upload import upload_bp

# print("Files in project:", os.listdir())
# print("Templates exists:", os.path.isdir("templates"))
# if os.path.isdir("templates"):
#     print("Templates folder contains:", os.listdir("templates"))
# print("Static exists:", os.path.isdir("static"))
# if os.path.isdir("static"):
#     print("Static folder contains:", os.listdir("static"))

app = Flask(__name__)

# print("Template folder:", app.template_folder)
# print("Template search path:", app.jinja_loader.searchpath)

app.config.from_object(Config)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": [
                "GET",
                "POST",
                "PUT",
                "DELETE",
                "OPTIONS",
            ],
            "allow_headers": "*",
        }
    },
)


@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Origin",
        "*",
    )

    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type,Authorization",
    )

    response.headers.add(
        "Access-Control-Allow-Methods",
        "GET,PUT,POST,DELETE,OPTIONS",
    )

    return response


os.makedirs(
    Config.UPLOAD_FOLDER,
    exist_ok=True,
)

app.register_blueprint(home_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(query_bp)
app.register_blueprint(documents_bp)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5500,
    )

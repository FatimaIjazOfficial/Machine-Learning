from flask import Blueprint,jsonify,render_template
from rag.process_documents import get_qa_chain

home_bp = Blueprint(
    "home",
    __name__,
)


@home_bp.route("/")
def home():
    return render_template("index.html")


@home_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "healthy",
            "documents_loaded": get_qa_chain() is not None,
        }
    )

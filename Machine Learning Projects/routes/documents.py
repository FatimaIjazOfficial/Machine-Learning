from flask import Blueprint,jsonify
from rag.process_documents import process_documents,clear_rag
from utils.helpers import list_uploaded_files,delete_uploaded_file,clear_upload_folder

documents_bp = Blueprint(
    "documents",
    __name__,
)


@documents_bp.route("/documents", methods=["GET"])
def list_documents():
    return jsonify(
        {
            "documents": list_uploaded_files()
        }
    ), 200


@documents_bp.route("/delete/<filename>", methods=["DELETE"])
def delete_document(filename):
    try:
        if not delete_uploaded_file(filename):
            return jsonify(
                {
                    "error": "File not found."
                }
            ), 404
        if not process_documents():
            clear_rag()
        return jsonify(
            {
                "message": f"{filename} deleted successfully."
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "error": str(e)
            }
        ), 500


@documents_bp.route("/clear", methods=["POST"])
def clear_documents():
    try:
        clear_upload_folder()
        clear_rag()
        return jsonify(
            {
                "message": "All documents cleared successfully."
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "error": str(e)
            }
        ), 500

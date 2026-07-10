from flask import Blueprint,jsonify,request
from rag.process_documents import process_documents
from utils.helpers import allowed_file,save_uploaded_file

upload_bp = Blueprint(
    "upload",
    __name__,
)


@upload_bp.route("/upload", methods=["POST"])
def upload_file():
    print("Upload request received")

    if "file" not in request.files:
        print("No file part")
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    print("Filename:", file.filename)

    if file.filename == "":
        print("Empty filename")
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        print("Invalid extension")
        return jsonify({"error": "Only PDF and TXT files are allowed."}), 400

    try:
        filename, path = save_uploaded_file(file)
        print("Saved:", path)

        print("Processing documents...")
        success = process_documents()
        print("Process result:", success)

        if not success:
            return jsonify({"error": "Failed to process documents."}), 500

        return jsonify({
            "message": "File uploaded successfully.",
            "filename": filename,
        })

    except Exception as e:
        print("UPLOAD ERROR:", e)
        raise

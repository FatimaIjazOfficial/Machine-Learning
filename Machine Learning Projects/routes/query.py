import os
from flask import Blueprint,jsonify,request
from rag.process_documents import get_qa_chain

query_bp = Blueprint(
    "query",
    __name__,
)


@query_bp.route("/query", methods=["POST"])
def query():
    qa_chain = get_qa_chain()
    if qa_chain is None:
        return jsonify(
            {"error": "No documents uploaded yet. Please upload documents first."}), 400
    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        return jsonify(
            { "error": "No question provided."}), 400
    try:
        result = qa_chain.invoke({"query": question})
        sources = list(
            {
                os.path.basename(doc.metadata.get("source", "Unknown"))
                for doc in result["source_documents"]
            }
        )
        return jsonify(
            {
                "answer": result["result"],
                "sources": sources,
            }
        ), 200
    except Exception as e:
        return jsonify(
            {"error": str(e)}), 500

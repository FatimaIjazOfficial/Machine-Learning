import os

from werkzeug.utils import secure_filename

from config import Config


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """

    return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower()
            in Config.ALLOWED_EXTENSIONS
    )


def get_upload_folder():
    """
    Create the uploads folder if it doesn't exist.
    """
    os.makedirs(
        Config.UPLOAD_FOLDER,
        exist_ok=True,
    )
    return Config.UPLOAD_FOLDER


def save_uploaded_file(file):
    """
    Save the uploaded file and return its path.
    """
    upload_folder = get_upload_folder()
    filename = secure_filename(file.filename)
    file_path = os.path.join(
        upload_folder,
        filename,
    )
    file.save(file_path)
    return filename, file_path


def list_uploaded_files():
    """
    Return information about uploaded files.
    """
    upload_folder = get_upload_folder()
    files = []
    for filename in os.listdir(upload_folder):
        path = os.path.join(
            upload_folder,
            filename,
        )
        if os.path.isfile(path):
            files.append(
                {
                    "name": filename,
                    "size": os.path.getsize(path),
                }
            )
    return files


def delete_uploaded_file(filename):
    """
    Delete a single uploaded file.
    """
    path = os.path.join(
        Config.UPLOAD_FOLDER,
        secure_filename(filename),
    )
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def clear_upload_folder():
    """
    Delete all uploaded files.
    """
    upload_folder = get_upload_folder()
    for filename in os.listdir(upload_folder):
        path = os.path.join(
            upload_folder,
            filename,
        )
        if os.path.isfile(path):
            os.remove(path)

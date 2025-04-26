from flask import Flask, request, send_from_directory, abort
import os

app = Flask(__name__)

# Secret token to access the files
VALID_TOKEN = "PeshwasCTF_SecretToken"

# Directory where flag files are stored (you can also use a subdirectory)
FLAG_DIRECTORY = "flag_files"

# Route to download files
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Check if the token is provided in the query string
    token = request.args.get('token')
    if token != VALID_TOKEN:
        abort(403, description="Forbidden: Invalid token")

    # Check if the file exists
    file_path = os.path.join(FLAG_DIRECTORY, filename)
    if os.path.exists(file_path):
        # Send the requested file
        return send_from_directory(FLAG_DIRECTORY, filename)
    else:
        abort(404, description="File not found")

if __name__ == '__main__':
    app.run(debug=True)

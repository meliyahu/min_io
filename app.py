from flask import Flask, request, render_template
from minio_local import MinIo
app = Flask(__name__)

#  bucket = ecoimages
#  file = Meteorology_1.png

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        req = request.form
        file_name = req["filename"]
        minio = MinIo("ecoimages", file_name)
        file_url = minio.get_url()
        return render_template("index.html", file_url=file_url)
    else:
        return render_template("index.html", file_url="")
    



if __name__ == "__main__":
    app.run(port=8080, debug=1)
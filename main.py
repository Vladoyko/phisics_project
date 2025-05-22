import flask

app = flask.Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def main():
    return flask.render_template("index.html")

@app.route("/download",methods = ["GET","POST"])
def download():
    return flask.send_file("Simulator.zip",as_attachment=True)
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)

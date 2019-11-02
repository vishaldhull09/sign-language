from flask import Flask, render_template, url_for, request, flash, redirect, Response
from camera import VideoCamera

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/predict", methods = ["POST"])
def predict():

    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
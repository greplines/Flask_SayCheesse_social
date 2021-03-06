from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
app.secret_key = "goodmanForWork8891"

camera = cv2.VideoCapture(0)  # use 0 for web camera

# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/secret')
def secret():
    """Video streaming home page."""
    return render_template('camera.html')

@app.route('/')
def ig():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/Gflix')
def gflix():
    """Video streaming home page."""
    return render_template('Gflix.html')


@app.route('/Gtok')
def Gtok():
    """Video streaming home page."""
    return render_template('Gtok.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template,Response
import cv2

fd = cv2.CascadeClassifier(r"haarcascadefiles/haarcascade_frontalface_alt.xml")

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def gen():
    vid = cv2.VideoCapture(0)
    while True:
        ret,img = vid.read()
        if ret ==True:
            faces = fd.detectMultiScale(img,1.1,5)
            if len(faces)>0:
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            ret,jpeg = cv2.imencode(".jpg",img)
            yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tostring() + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
    
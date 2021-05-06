#Import necessary libraries
from flask import Flask, render_template, Response
import cv2

#Initialize the Flask app
app = Flask(__name__)

atcs = ['Aceh', 'Anggrek', 'Banda', 'Batununggal', 'Buahbatu', 'Cibaduyut', 'Cibeureum', 'Cicaheum', 'CihampelasBarat', 'CihampelasPTZ', 'CihampelasTimur', 'CihampelasUtara', 'Cihapit', 'Cikapayang1', 'CikapayangSelatan', 'CikapayangUtara', 'Cikutra', 'Cimuncang', 'Cipaganti', 'Cipaganti2', 'Gardujati', 'Gedebage', 'GudangUtara', 'Jamika', 'Kopo', 'KopoPeta', 'Laswi', 'Lombok', 'MerdekaAceh', 'MerdekaJuanda', 'MochToha', 'Otista', 'Padasuka', 'Pahlawan', 'PasarCaringin', 'PasirKalikiIP', 'PasirKoja', 'RamdanBkrBarat', 'Ruasanggrek', 'Ruasbanda', 'Ruasbandaistiqomah', 'Ruascihapitpramuka', 'Ruasgardujati', 'Ruasistiqomahbanda', 'Ruasistiqomahcihapit', 'Ruasotista', 'Ruaspramukacihapit', 'Ruastrunojoyo', 'Samsat', 'SimpangLima', 'Sulanjana', 'Supratman', 'Tamansari', 'Tamblong', 'Telkom', 'TolPasteur', 'Trunojoyo', 'UjungBerung', 'UtaraLaswi', 'alunpelajar', 'laswisukabumi', 'timur']


def gen_frames(location):
    if location not in atcs: return None
      
    camera = cv2.VideoCapture('http://45.118.114.26/camera/{}.m3u8'.format(location))

    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # concat frame one by one and show result
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
  
@app.route('/<location>')
def index(location):
    if not location: location = 'PasirKalikiIP'
    return render_template('index.html', atcs=atcs, location=location)


@app.route('/video_feed/<location>')
def video_feed(location):
    return Response(gen_frames(location),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

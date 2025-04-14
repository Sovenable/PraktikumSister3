from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate("SDK_key.json")  # path file SDK key firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cloud-pert3-c77ac-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Ganti dengan URL firebase realtime
})

# Referensi ke data sensor
ref = db.reference('/WaterDistance')

@app.route('/')
def index():
    """Menampilkan halaman monitoring"""
    snapshot = ref.get()  # Ambil data terbaru
    distance = snapshot if snapshot else "Data belum tersedia"
    return render_template('index.html', distance=distance)

@app.route('/data')
def get_data():
    """API untuk mengambil data terbaru dalam format JSON"""
    snapshot = ref.get()
    data = {'distance': snapshot} if snapshot else {'distance': "Data belum tersedia"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
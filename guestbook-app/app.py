import os
from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(__name__)

# Mengambil host Redis dari environment variable yang akan di-set oleh Kubernetes
# Jika tidak ada, gunakan 'localhost' sebagai default (untuk tes lokal)
redis_host = os.environ.get('REDIS_HOST', 'localhost')

try:
    # Koneksi ke server Redis
    r = redis.Redis(host=redis_host, port=6379, db=0, socket_connect_timeout=2)
    r.ping()
    print(f"Berhasil terhubung ke Redis di {redis_host}")
except redis.exceptions.ConnectionError as e:
    print(f"Gagal terhubung ke Redis di {redis_host}: {e}")
    r = None # Set 'r' ke None jika koneksi gagal

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = []
    if request.method == 'POST':
        if r:
            # Ambil pesan dari form dan simpan ke Redis
            message = request.form['message']
            r.rpush('messages', message)
        return redirect(url_for('index'))

    if r:
        # Ambil semua pesan dari Redis untuk ditampilkan
        message_bytes = r.lrange('messages', 0, -1)
        messages = [msg.decode('utf-8') for msg in message_bytes]
        messages.reverse() # Tampilkan pesan terbaru di atas

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    # Jalankan di host 0.0.0.0 agar bisa diakses dari dalam kontainer
    app.run(host='0.0.0.0', port=5000)

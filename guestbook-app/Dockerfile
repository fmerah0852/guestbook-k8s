# 1. Gunakan base image Python yang ringan
FROM python:3.9-slim

# 2. Set direktori kerja di dalam kontainer
WORKDIR /app

# 3. Salin file requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Salin sisa kode aplikasi ke dalam direktori kerja
COPY . .

# 5. Tentukan port yang akan diekspos oleh kontainer
EXPOSE 5000

# 6. Perintah untuk menjalankan aplikasi saat kontainer dimulai
CMD ["python", "app.py"]

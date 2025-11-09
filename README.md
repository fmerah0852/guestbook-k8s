# 🚀 Guestbook: Aplikasi Web (Flask + Redis) di Kubernetes dengan CI/CD

Proyek ini adalah implementasi aplikasi web *guestbook* sederhana yang dibangun menggunakan arsitektur *microservice* (frontend Flask dan backend Redis).

Tujuan utama dari proyek ini adalah untuk mendemonstrasikan dan mempraktikkan alur kerja DevOps *end-to-end*:
1.  **Kontainerisasi** aplikasi web menggunakan Docker.
2.  **Orkestrasi** kontainer di klaster Kubernetes (dijalankan secara lokal di Minikube).
3.  **Otomatisasi Build (CI)** menggunakan GitHub Actions untuk me-build dan me-push *image* ke Docker Hub.
4.  **Paparan Layanan (Networking)** profesional menggunakan NGINX Ingress Controller.

---

## 🛠️ Teknologi & Arsitektur

Proyek ini menggunakan tumpukan teknologi berikut:

* **Frontend:** Python (Flask)
* **Backend (Database):** Redis
* **Kontainerisasi:** Docker
* **Orkestrasi:** Kubernetes (Minikube)
* **CI/CD Pipeline:** GitHub Actions
* **Container Registry:** Docker Hub
* **Ingress (Jaringan):** NGINX Ingress Controller

Nama : Hafizh Naufal Nuha Kusuma
 
NIM : A11.2023.14904

# Simple LMS API

## A. Cara Menjalankan

```bash
# Clone repository
git clone <repo-url>
cd simple-lms-restAPI

# Jalankan Docker
docker-compose up --build

# Install dependencies
docker-compose exec app pip install django-ninja
docker-compose exec app pip install PyJWT

# Jalankan migrasi database
docker-compose exec app python manage.py migrate

# Seed data awal
docker-compose exec app python manage.py seed_data

# Jalankan di background
docker-compose up -d
```

API tersedia di: `http://localhost:8000/api/docs`

---

## B. Dokumentasi API

### 1. POST `/api/auth/register` — Register User Baru
![Register](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/Register.png)

### 2. POST `/api/auth/login` — Login
![Login](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/Login.png)

### 3. POST `/api/auth/refresh` — Refresh Token
![Refresh Token](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/Refresh.png)

### 4. GET `/api/auth/me` — Lihat Profil
![Get Me](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/GET%20me.png)

### 5. PUT `/api/auth/me` — Update Profil
![Update Me](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/PUT%20me.png)

### 6. GET `/api/courses` — List Kursus
![List Courses](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/GET%20Courses.png)

### 7. POST `/api/courses` — Buat Kursus (Instructor)
![Create Course](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/POST%20Courses.png)

### 8. GET `/api/courses/{id}` — Detail Kursus
![Detail Course](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/GET%20Detail%20Kursus.png)

### 9. PATCH `/api/courses/{id}` — Update Kursus (Owner)
![Update Course](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/PATCH%20Update.png)

### 10. DELETE `/api/courses/{id}` — Hapus Kursus (Admin)
![Delete Course](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/DELETE%20Kursus.png)

### 11. POST `/api/enrollments` — Enroll Kursus (Student)
![Enroll](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/POST%20Enroll.png)

### 12. GET `/api/enrollments/my-courses` — Kursus Saya
![My Courses](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/GET%20Kursus%20Saya.png)

### 13. POST `/api/enrollments/{id}/progress` — Tandai Selesai
![Progress](https://raw.githubusercontent.com/hafizh1119/simple-lms-api/main/Dokumentasi/POST%20Progress.png)

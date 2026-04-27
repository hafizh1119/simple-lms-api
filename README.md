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
![Register](01_register.png)

### 2. POST `/api/auth/login` — Login
![Login](02_login.png)

### 3. POST `/api/auth/refresh` — Refresh Token
![Refresh Token](03_refresh_token.png)

### 4. GET `/api/auth/me` — Lihat Profil
![Get Me](04_get_me.png)

### 5. PUT `/api/auth/me` — Update Profil
![Update Me](05_update_me.png)

### 6. GET `/api/courses` — List Kursus
![List Courses](06_list_courses.png)

### 7. POST `/api/courses` — Buat Kursus (Instructor)
![Create Course](07_create_course.png)

### 8. GET `/api/courses/{id}` — Detail Kursus
![Detail Course](08_detail_course.png)

### 9. PATCH `/api/courses/{id}` — Update Kursus (Owner)
![Update Course](09_update_course.png)

### 10. DELETE `/api/courses/{id}` — Hapus Kursus (Admin)
![Delete Course](10_delete_course.png)

### 11. POST `/api/enrollments` — Enroll Kursus (Student)
![Enroll](11_enroll.png)

### 12. GET `/api/enrollments/my-courses` — Kursus Saya
![My Courses](12_my_courses.png)

### 13. POST `/api/enrollments/{id}/progress` — Tandai Selesai
![Progress](13_progress.png)

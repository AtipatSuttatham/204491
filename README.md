# LMS (Learning Management System)

ระบบ LMS ออนไลน์ ลักษณะคล้าย Mango CMU — แบ่งสิทธิ์ผู้ใช้ 3 ระดับ: Administrator, Teacher/Instructor, Student

## Tech Stack

| ส่วน | เทคโนโลยี |
|---|---|
| Backend | Django 5.2 + Django REST Framework, JWT (`djangorestframework-simplejwt`) |
| Frontend | React + Vite + TypeScript + Tailwind CSS v4 *(ยังไม่ scaffold)* |
| Database | PostgreSQL 16 (dev ผ่าน Docker) |
| File storage | Cloudinary (รูป/เอกสาร/วิดีโอ) + รองรับแปะลิงก์ YouTube |
| Package manager | `uv` (backend) · `pnpm` (frontend) |

## โครงสร้าง repo

```
/backend    Django + DRF        (ดู backend/README.md)
/frontend   React + Vite + TS   (จะเพิ่มใน chunk ถัดไป)
/docs       เอกสารออกแบบฐานข้อมูล (database.md v1.3 — freeze แล้ว)
```

## เริ่มต้นเร็ว

```bash
docker compose up -d          # Postgres (host port 5433)
cd backend && cp .env.example .env && uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

รายละเอียดข้อกำหนดโปรเจกต์: [`CLAUDE.md`](./CLAUDE.md)

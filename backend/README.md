# LMS — Backend (Django 5.2 + DRF)

## ต้องมีก่อน

- Python 3.13 (`uv` จัดการให้ได้)
- [`uv`](https://docs.astral.sh/uv/)
- PostgreSQL — ผ่าน `docker compose` ที่ root ของ repo (host port **5433**)

## เริ่มใช้งาน (dev)

```bash
# 1. ฐานข้อมูล (จาก root ของ repo)
docker compose up -d

# 2. ตั้งค่า env
cd backend
cp .env.example .env

# 3. ติดตั้ง dependencies
uv sync

# 4. migrate + สร้าง superuser
uv run python manage.py migrate
uv run python manage.py createsuperuser

# 5. รัน dev server
uv run python manage.py runserver
```

- API health check: <http://localhost:8000/api/health/>
- Django admin: <http://localhost:8000/admin/>

## ทดสอบ / lint

```bash
uv run pytest          # ต้องมี Postgres (ดู pytest --reuse-db)
uv run ruff check .
uv run ruff format .
```

## โครงสร้าง

```
config/            Django project (settings แยก base/dev/test/prod, urls, wsgi, asgi)
common/            abstract models: TimeStampedModel, Auditable, SoftDeleteModel
accounts/          User (custom), EmailVerificationToken
academics/ content/ enrollment/ assessments/ assignments/
grading/ announcements/ notifications/ audit/     ← โดเมนอื่น (ยังเป็นโครง — models เพิ่มตาม feature slice)
```

การออกแบบฐานข้อมูลทั้งหมด: [`../docs/database.md`](../docs/database.md) (v1.3, freeze แล้ว)

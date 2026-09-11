# LMS — Frontend (React + Vite + TypeScript + Tailwind v4)

## ต้องมีก่อน

- Node.js 24+
- `pnpm` (ดู `packageManager` ใน `package.json`)
- Backend รันอยู่ที่ `http://localhost:8000` (ดู `../backend/README.md`)

## เริ่มใช้งาน (dev)

```bash
cd frontend
cp .env.example .env.local
pnpm install
pnpm dev
```

เปิด <http://localhost:5173> — หน้าแรกจะเช็คสถานะเชื่อมต่อ backend ผ่าน `/api/health/`

## คำสั่งอื่น

```bash
pnpm typecheck   # tsc -b --noEmit
pnpm lint        # eslint .
pnpm test        # vitest run
pnpm build       # production build
```

## โครงสร้าง

```
src/
  i18n/            react-i18next — ไทย (default) / อังกฤษ (src/i18n/locales/*.json)
  lib/api.ts       axios instance กลาง (แนบ JWT อัตโนมัติ)
  components/      ส่วนประกอบ UI ที่ใช้ร่วม
  pages/           หน้าจอ (ผูกกับ route ใน App.tsx)
  test/setup.ts    vitest + testing-library setup
```

หน้าจอของแต่ละ role (Admin/Teacher/Student) จะเพิ่มตาม feature slice — ดูภาพรวมโปรเจกต์ที่ [`../CLAUDE.md`](../CLAUDE.md)

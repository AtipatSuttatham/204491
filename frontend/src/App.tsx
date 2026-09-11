import { Route, Routes } from 'react-router'

import HomePage from './pages/HomePage'
import NotFoundPage from './pages/NotFoundPage'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      {/* route ของแต่ละ role (Admin/Teacher/Student) จะเพิ่มตาม feature slice */}
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  )
}

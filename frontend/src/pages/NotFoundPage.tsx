import { useTranslation } from 'react-i18next'
import { Link } from 'react-router'

export default function NotFoundPage() {
  const { t } = useTranslation()

  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-4 bg-slate-50 px-4 text-center">
      <p className="text-6xl font-bold text-slate-300">404</p>
      <h1 className="text-xl font-semibold text-slate-700">{t('notFound.title')}</h1>
      <Link to="/" className="text-sm font-medium text-blue-600 hover:underline">
        {t('notFound.backHome')}
      </Link>
    </div>
  )
}

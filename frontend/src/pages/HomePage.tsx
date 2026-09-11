import { useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'

import LanguageSwitcher from '../components/LanguageSwitcher'
import { api } from '../lib/api'

type HealthStatus = 'loading' | 'ok' | 'error'

export default function HomePage() {
  const { t } = useTranslation()
  const [status, setStatus] = useState<HealthStatus>('loading')

  useEffect(() => {
    let cancelled = false
    api
      .get('/health/')
      .then(() => {
        if (!cancelled) setStatus('ok')
      })
      .catch(() => {
        if (!cancelled) setStatus('error')
      })
    return () => {
      cancelled = true
    }
  }, [])

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="flex items-center justify-between border-b border-slate-200 bg-white px-6 py-4">
        <span className="text-lg font-semibold text-slate-800">{t('app.name')}</span>
        <LanguageSwitcher />
      </header>

      <main className="mx-auto flex max-w-xl flex-col items-center gap-6 px-4 py-24 text-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">{t('home.title')}</h1>
          <p className="mt-2 text-slate-600">{t('home.subtitle')}</p>
        </div>

        <div
          data-testid="backend-status"
          className={`rounded-full px-4 py-1.5 text-sm font-medium ${
            status === 'ok'
              ? 'bg-green-100 text-green-700'
              : status === 'error'
                ? 'bg-red-100 text-red-700'
                : 'bg-slate-100 text-slate-500'
          }`}
        >
          {t('home.backendStatus')}:{' '}
          {status === 'loading'
            ? t('common.loading')
            : status === 'ok'
              ? t('home.backendOk')
              : t('home.backendError')}
        </div>
      </main>
    </div>
  )
}

import { useTranslation } from 'react-i18next'

const LANGUAGES = [
  { code: 'th', label: 'ไทย' },
  { code: 'en', label: 'English' },
] as const

export default function LanguageSwitcher() {
  const { i18n, t } = useTranslation()

  return (
    <label className="flex items-center gap-2 text-sm text-slate-600">
      <span className="sr-only">{t('common.language')}</span>
      <select
        value={i18n.resolvedLanguage}
        onChange={(e) => void i18n.changeLanguage(e.target.value)}
        className="rounded-md border border-slate-300 bg-white px-2 py-1 text-sm focus:border-blue-500 focus:outline-none"
      >
        {LANGUAGES.map((lang) => (
          <option key={lang.code} value={lang.code}>
            {lang.label}
          </option>
        ))}
      </select>
    </label>
  )
}

import { render, screen, waitFor } from '@testing-library/react'
import { beforeEach, describe, expect, it, vi } from 'vitest'

import i18n from '../i18n'
import { api } from '../lib/api'
import HomePage from './HomePage'

vi.mock('../lib/api', () => ({
  api: { get: vi.fn() },
}))

describe('HomePage', () => {
  // jsdom ใช้ locale en-US เป็นค่าเริ่มต้น — บังคับเป็นไทยให้ตรงกับ default ของแอป
  beforeEach(() => {
    void i18n.changeLanguage('th')
  })

  it('shows backend OK status when health check succeeds', async () => {
    vi.mocked(api.get).mockResolvedValueOnce({ data: { status: 'ok' } })

    render(<HomePage />)

    await waitFor(() =>
      expect(screen.getByTestId('backend-status')).toHaveTextContent('เชื่อมต่อสำเร็จ'),
    )
  })

  it('shows backend error status when health check fails', async () => {
    vi.mocked(api.get).mockRejectedValueOnce(new Error('network error'))

    render(<HomePage />)

    await waitFor(() =>
      expect(screen.getByTestId('backend-status')).toHaveTextContent('เชื่อมต่อไม่ได้'),
    )
  })
})

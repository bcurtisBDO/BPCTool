import { afterEach, describe, expect, it, vi } from 'vitest'
import { authHeader, buildAdoApiBase, fetchProjects, maskSecret } from './adoApi'

describe('adoApi helpers', () => {
  afterEach(() => {
    vi.unstubAllGlobals()
    vi.restoreAllMocks()
  })

  it('builds Basic auth with empty username', () => {
    expect(authHeader('secret-token')).toBe(`Basic ${btoa(':secret-token')}`)
  })

  it('masks secrets', () => {
    expect(maskSecret('abcdefghij')).toBe('abcd***ij')
  })

  it('builds proxy API base from org URL', () => {
    expect(buildAdoApiBase('https://contoso.visualstudio.com')).toBe('/ado-proxy/contoso')
    expect(buildAdoApiBase('contoso')).toBe('/ado-proxy/contoso')
  })

  it('fetchProjects maps ADO payload', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn(async () => ({
        ok: true,
        status: 200,
        statusText: 'OK',
        headers: {
          get: (name) => (name === 'content-type' ? 'application/json' : null),
        },
        json: async () => ({
          value: [
            { id: '1', name: 'Alpha' },
            { id: '2', name: 'Beta' },
          ],
        }),
      })),
    )

    const projects = await fetchProjects('https://dev.azure.com/contoso', '01234567890123456789')
    expect(projects).toEqual([
      { id: '1', name: 'Alpha', state: undefined },
      { id: '2', name: 'Beta', state: undefined },
    ])
    expect(fetch).toHaveBeenCalledWith(
      '/ado-proxy/contoso/_apis/projects?api-version=7.1',
      expect.objectContaining({
        method: 'GET',
        headers: expect.objectContaining({
          Authorization: authHeader('01234567890123456789'),
        }),
      }),
    )
  })
})

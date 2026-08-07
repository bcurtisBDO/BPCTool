import { describe, expect, it } from 'vitest'
import { normalizeAdoOrgUrl, parseAdoOrgUrl } from './adoOrgUrl'

describe('parseAdoOrgUrl', () => {
  it('parses dev.azure.com URLs', () => {
    expect(parseAdoOrgUrl('https://dev.azure.com/contoso')).toEqual({
      ok: true,
      org: 'contoso',
      canonicalUrl: 'https://dev.azure.com/contoso',
      apiHostname: 'dev.azure.com',
    })
  })

  it('parses visualstudio.com and bare org names', () => {
    expect(parseAdoOrgUrl('https://contoso.visualstudio.com').org).toBe('contoso')
    expect(parseAdoOrgUrl('contoso').canonicalUrl).toBe('https://dev.azure.com/contoso')
  })

  it('rejects unsupported hosts', () => {
    expect(parseAdoOrgUrl('https://example.com/org').ok).toBe(false)
  })
})

describe('normalizeAdoOrgUrl', () => {
  it('preserves visualstudio host style', () => {
    expect(normalizeAdoOrgUrl('https://contoso.visualstudio.com/extra')).toEqual({
      ok: true,
      url: 'https://contoso.visualstudio.com',
    })
  })

  it('canonicalizes bare org names to dev.azure.com', () => {
    expect(normalizeAdoOrgUrl('contoso')).toEqual({
      ok: true,
      url: 'https://dev.azure.com/contoso',
    })
  })
})

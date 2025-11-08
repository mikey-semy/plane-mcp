# SSE Connection Fix - Credentials in URL Not Supported

## Problem

The error occurs because modern MCP clients using the Fetch API cannot construct requests with credentials embedded in the URL:

```
Error: Request cannot be constructed from a URL that includes credentials:
http://admin:Pvxk7mjqjg9!@mcp-plane-e2jgos-367e9c-62-60-246-35.traefik.me:9000/sse
```

This is a security restriction in the Fetch API - credentials cannot be passed as `http://user:pass@host/path`.

## Solution

Use the `Authorization` header instead of embedding credentials in the URL.

## Your Configuration Fix

### Current (Not Working) ❌
```json
{
  "servers": {
    "plane": {
      "url": "http://admin:Pvxk7mjqjg9!@mcp-plane-e2jgos-367e9c-62-60-246-35.traefik.me:9000/sse"
    }
  }
}
```

### Fixed (Working) ✅
```json
{
  "servers": {
    "plane": {
      "url": "http://mcp-plane-e2jgos-367e9c-62-60-246-35.traefik.me:9000/sse",
      "headers": {
        "Authorization": "Basic YWRtaW46UHZ4azdtanFqZzkh"
      }
    }
  }
}
```

## Important Notes

1. **Remove credentials from URL**: The URL should NOT include `admin:password@`
2. **Add Authorization header**: Use `Basic <base64_encoded_credentials>`
3. **Use HTTPS in production**: Your current URL uses `http://` - switch to `https://` for security

## How to Generate Authorization Header

For any username:password combination, use one of the provided scripts:

### PowerShell (Windows)
```powershell
.\scripts\generate-auth-header.ps1 -Username "admin" -Password "Pvxk7mjqjg9!"
```

### Bash (Linux/macOS)
```bash
./scripts/generate-auth-header.sh admin "Pvxk7mjqjg9!"
```

## Updated Documentation

The following files have been updated with the correct configuration format:
- `docs/SSE_AUTH.md` - Complete Basic Auth guide
- `README.md` - Main documentation with examples
- `scripts/generate-auth-header.ps1` - PowerShell helper script
- `scripts/generate-auth-header.sh` - Bash helper script

## Testing the Fix

After updating your configuration:

1. Save the changes to your `mcp.json` or VSCode settings
2. Restart VSCode or reload the window
3. The connection should work without the Fetch API error

You can test the endpoint with curl to verify it's working:
```bash
curl -H "Authorization: Basic YWRtaW46UHZ4azdtanFqZzkh" \
  http://mcp-plane-e2jgos-367e9c-62-60-246-35.traefik.me:9000/sse
```

## Security Recommendations

1. ✅ Switch from `http://` to `https://`
2. ✅ Use strong passwords (your current password is good!)
3. ✅ Don't commit credentials to git
4. ✅ Consider IP whitelisting if possible
5. ✅ Rotate passwords regularly

## References

- [SSE_AUTH.md](../docs/SSE_AUTH.md) - Complete authentication guide
- [MDN: Fetch API Security](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/servers)

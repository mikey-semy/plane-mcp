#!/bin/bash
# Script to generate Basic Auth header for MCP SSE connection
# Usage: ./generate-auth-header.sh username password

if [ $# -ne 2 ]; then
    echo "Usage: $0 <username> <password>"
    echo "Example: $0 admin SecurePassword123"
    exit 1
fi

USERNAME=$1
PASSWORD=$2

echo "Generating Basic Auth header..."
echo ""

CREDENTIALS="${USERNAME}:${PASSWORD}"
BASE64=$(echo -n "$CREDENTIALS" | base64)
AUTH_HEADER="Basic $BASE64"

echo "✅ Generated Authorization header:"
echo "$AUTH_HEADER"
echo ""

echo "Add this to your mcp.json configuration:"
cat << EOF
{
  "servers": {
    "plane": {
      "url": "https://your-server-url:9000/sse",
      "headers": {
        "Authorization": "$AUTH_HEADER"
      }
    }
  }
}
EOF

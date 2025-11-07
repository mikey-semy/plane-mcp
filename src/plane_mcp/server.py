"""Main MCP server implementation with FastMCP."""

import os
import sys

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from plane_mcp.common.version import get_version
from plane_mcp.tools.cycle_issues import register_cycle_issue_tools
from plane_mcp.tools.cycles import register_cycle_tools
from plane_mcp.tools.issues import register_issue_tools
from plane_mcp.tools.metadata import register_metadata_tools
from plane_mcp.tools.module_issues import register_module_issue_tools
from plane_mcp.tools.modules import register_module_tools
from plane_mcp.tools.projects import register_project_tools
from plane_mcp.tools.user import register_user_tools
from plane_mcp.tools.worklogs import register_worklog_tools

# Load environment variables
load_dotenv()

# Validate required environment variables
required_vars = ["PLANE_API_KEY", "PLANE_WORKSPACE_SLUG"]
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"ERROR: Missing required environment variables: {', '.join(missing_vars)}", file=sys.stderr)
    sys.exit(1)

# Get configuration
version = get_version()
host = os.getenv("MCP_HOST", "0.0.0.0")
port = int(os.getenv("MCP_PORT", "8000"))
transport = os.getenv("MCP_TRANSPORT", "stdio")

# Create FastMCP server
mcp = FastMCP(
    name="plane-mcp-server",
    instructions=f"Plane MCP Server v{version} - Integration with Plane project management platform",
    host=host,
    port=port,
)

# Register all tools
register_metadata_tools(mcp)
register_user_tools(mcp)
register_project_tools(mcp)
register_issue_tools(mcp)
register_module_tools(mcp)
register_module_issue_tools(mcp)
register_cycle_tools(mcp)
register_cycle_issue_tools(mcp)
register_worklog_tools(mcp)


def main() -> None:
    """Main entry point for the server."""
    print(f"Starting Plane MCP Server v{version}", file=sys.stderr)
    print(f"Server listening on {host}:{port} (transport: {transport})", file=sys.stderr)
    print("Registered tools: metadata, user, projects, issues, modules, module-issues, cycles, cycle-issues, worklogs", file=sys.stderr)

    try:
        # Run the server with configured transport (blocks until stopped)
        mcp.run(transport=transport)
    except KeyboardInterrupt:
        print("\nShutting down Plane MCP Server...", file=sys.stderr)
    except Exception as e:
        print(f"ERROR: Server crashed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

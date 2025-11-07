FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml ./
COPY src ./src

# Install dependencies
RUN uv sync --frozen

# Expose port for SSE transport
EXPOSE 8000

# Set environment variables
ENV MCP_TRANSPORT=sse
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000

# Run the server
CMD ["uv", "run", "plane-mcp"]

# Ivan Paner Resume MCP

A small FastMCP server that exposes Ivan Paner's resume details as MCP tools.

The deployed Remote MCP server URL is:

- `https://resume.ivanpaner.com/mcp`

## Local development

### Prerequisites

- Python `>= 3.13`
- `uv` (<https://github.com/astral-sh/uv>)

### Install

```bash
uv sync --locked
```

### Run

```bash
uv run uvicorn src.server:app --reload --host 0.0.0.0 --port 8000
```

Then open:

- `http://localhost:8000/` (status page)
- `http://localhost:8000/health` (health check)

## Docker

```bash
docker build -t resume-mcp .
docker run --rm -p 8000:8000 resume-mcp
```

## Lint

```bash
uv run ruff check .
```

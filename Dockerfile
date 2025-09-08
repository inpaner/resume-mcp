FROM ghcr.io/astral-sh/uv:python3.13-alpine
# ENV UV_COMPILE_BYTECODE=1
# ENV UV_LINK_MODE=copy
# ENV UV_TOOL_BIN_DIR=/usr/local/bin
# RUN --mount=type=cache,id=s/c85302c3-0953-4f19-bb59-65a0d14aa2ad-/root/.cache/uv,target=/root/.cache/uv \
#   --mount=type=bind,id=s/c85302c3-0953-4f19-bb59-65a0d14aa2ad-uv.lock,source=uv.lock,target=uv.lock \
#   --mount=type=bind,id=s/c85302c3-0953-4f19-bb59-65a0d14aa2ad-pyproject.toml,source=pyproject.toml,target=pyproject.toml \
#   uv sync --locked --no-install-project --no-dev
# RUN uv sync --locked --no-install-project --no-dev
ADD . /app
WORKDIR /app
# RUN --mount=type=cache,target=/root/.cache/uv \
#   uv sync --locked --no-dev
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT []
EXPOSE 8000
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]

FROM ghcr.io/astral-sh/uv:python3.13-alpine

ADD . /app
WORKDIR /app

# Run the service as a non-root user.
RUN addgroup -S app \
  && adduser -S app -G app \
  && mkdir -p /tmp/uv-cache \
  && chown -R app:app /app /tmp/uv-cache

USER app
ENV UV_CACHE_DIR=/tmp/uv-cache
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT []
EXPOSE 8000
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]

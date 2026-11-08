# Reference container: local gateway only. Use a trusted TLS reverse proxy and
# external identity/approval services before any public exposure.
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY . /app
RUN groupadd --system agent && useradd --system --gid agent agent \
    && mkdir -p /var/lib/agent && chown agent:agent /var/lib/agent
USER agent
ENV AGENT_STATE_DB=/var/lib/agent/state.sqlite3
EXPOSE 8765
CMD ["python", "-m", "runtime.gateway"]

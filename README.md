# Multi Model Chat Gateway

A learning project for a small gateway over OpenAI-compatible APIs and Ollama.

> Status: initial scaffold. Provider adapters and streaming chat are not implemented yet.

## Planned scope

- Unified model-list and chat endpoints
- OpenAI-compatible and Ollama providers
- Server-Sent Events streaming
- Timeout, upstream-error, and client-disconnect handling
- User/admin authorization and conversation ownership
- Request-state logging and pytest coverage

## Upstream reference

Product behavior and integration patterns are studied from [open-webui/open-webui](https://github.com/open-webui/open-webui). This repository is an independent personal implementation and does not claim participation in the upstream project.

## Run locally

```bash
python -m venv .venv
pip install -e ".[dev]"
uvicorn app.main:app --reload
pytest
```

Open <http://127.0.0.1:8000/docs> after startup.

## Docker

```bash
docker build -t multi-model-chat-gateway .
docker run --rm -p 8000:8000 multi-model-chat-gateway
```

## Roadmap

1. Define a minimal provider protocol.
2. Add OpenAI-compatible non-streaming chat.
3. Add Ollama and SSE streaming.
4. Add authorization, logs, and failure tests.

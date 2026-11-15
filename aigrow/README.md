# AIGROW for Hermes Agent

[AIGROW](https://aigrow.gg/ai-api) sells prepaid API credit for Claude, GPT, Gemini and
Grok models behind one OpenAI-compatible endpoint, `https://aigrow.gg/v1`. This plugin
registers it as a Hermes model provider.

## Setup

1. Buy API credit and create a key at https://aigrow.gg/ai-api.
2. Install the plugin with `hermes plugins install aigrow`. Hermes asks for `AIGROW_API_KEY`.
3. Run `hermes model` and pick AIGROW, or start a chat with:

```bash
hermes chat --provider aigrow --model claude-sonnet-5.5
```

## Models

The model picker reads the live list from `https://aigrow.gg/v1/models` with your key.
When that call fails, it falls back to these ids:

- `claude-opus-5.5`, `claude-sonnet-5.5`, `claude-fable-5.2`, `claude-fable-5.1`
- `gpt-6.1-sol`, `gpt-6.1-terra`, `gpt-6-astra`
- `gemini-4-argon`
- `grok-4.7`

Context windows, prices and capabilities for these ids are published on
[models.dev](https://models.dev) under the provider id `aigrow`, which Hermes reads for
model metadata. Auxiliary tasks (compression, titles) default to `gpt-6.1-terra`, the
cheapest model in the list.

## What the plugin does

It registers one model provider when Hermes imports it, and nothing else: no tools,
hooks, middleware, commands, background work, telemetry or file access. Chat requests
(prompts, tool schemas and results, images for models that accept them) and the model
list request go to `https://aigrow.gg/v1` through Hermes's own client, authenticated with
`AIGROW_API_KEY`, which Hermes reads. Usage is billed to your AIGROW credit. The plugin
opens no connections of its own and does not update itself.

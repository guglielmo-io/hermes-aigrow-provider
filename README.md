# Hermes AIGROW provider

Model-provider plugin for [Hermes Agent](https://github.com/NousResearch/hermes-agent).
It registers [AIGROW](https://aigrow.gg/ai-api) as an OpenAI-compatible provider, so
`hermes model` lists it and `--provider aigrow` works.

The plugin itself lives in [`aigrow/`](aigrow/); see its README for setup and models.

## Install

After the plugin is listed in the Hermes catalog:

```bash
hermes plugins install aigrow
```

Manual installation:

```bash
git clone https://github.com/guglielmo-io/hermes-aigrow-provider.git
mkdir -p ~/.hermes/plugins/model-providers
cp -r hermes-aigrow-provider/aigrow ~/.hermes/plugins/model-providers/aigrow
```

## Development

```bash
python -m unittest discover -s tests -v
```

The tests are offline and use a minimal stub of the Hermes provider registry.

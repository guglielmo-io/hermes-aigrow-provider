"""Offline contract tests for the AIGROW Hermes provider."""

from __future__ import annotations

import importlib.util
import sys
import types
import unittest
from dataclasses import dataclass
from pathlib import Path


@dataclass
class _ProviderProfile:
    name: str
    aliases: tuple = ()
    display_name: str = ""
    description: str = ""
    signup_url: str = ""
    env_vars: tuple = ()
    base_url: str = ""
    models_url: str = ""
    auth_type: str = "api_key"
    default_aux_model: str = ""
    fallback_models: tuple = ()


# Model ids published for the provider at https://models.dev/api.json ("aigrow").
MODELS_DEV_IDS = {
    "claude-fable-5.1",
    "claude-fable-5.2",
    "claude-opus-5.5",
    "claude-sonnet-5.5",
    "gemini-4-argon",
    "gpt-6-astra",
    "gpt-6.1-sol",
    "gpt-6.1-terra",
    "grok-4.7",
}


class AigrowProfileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registered = []
        providers = types.ModuleType("providers")
        providers.register_provider = cls.registered.append
        base = types.ModuleType("providers.base")
        base.ProviderProfile = _ProviderProfile
        sys.modules["providers"] = providers
        sys.modules["providers.base"] = base

        plugin = Path(__file__).parents[1] / "aigrow" / "__init__.py"
        spec = importlib.util.spec_from_file_location("aigrow", plugin)
        assert spec and spec.loader
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def test_registers_one_provider(self) -> None:
        self.assertEqual(self.registered, [self.module.aigrow])

    def test_name_matches_models_dev_provider_id(self) -> None:
        self.assertEqual(self.module.aigrow.name, "aigrow")

    def test_uses_the_public_endpoint(self) -> None:
        self.assertEqual(self.module.aigrow.base_url, "https://aigrow.gg/v1")
        self.assertEqual(self.module.aigrow.models_url, "https://aigrow.gg/v1/models")
        self.assertEqual(self.module.aigrow.env_vars, ("AIGROW_API_KEY",))

    def test_fallback_models_match_models_dev(self) -> None:
        models = self.module.aigrow.fallback_models
        self.assertEqual(len(models), len(set(models)))
        self.assertEqual(set(models), MODELS_DEV_IDS)

    def test_aux_model_is_in_the_list(self) -> None:
        self.assertIn(self.module.aigrow.default_aux_model, self.module.aigrow.fallback_models)


if __name__ == "__main__":
    unittest.main()

import shutil
import os
import sublime

from LSP.plugin.core.handlers import LanguageHandler
from LSP.plugin.core.settings import ClientConfig, read_client_config
from lsp_utils import ServerNpmResource
from .schemas import schemas

PACKAGE_NAME = 'LSP-json'
SETTINGS_FILENAME = 'LSP-json.sublime-settings'
SERVER_DIRECTORY = 'vscode-json-languageserver'
SERVER_BINARY_PATH = os.path.join(SERVER_DIRECTORY, 'node_modules', 'vscode-json-languageserver',
                                  'bin', 'vscode-json-languageserver')

server = ServerNpmResource(PACKAGE_NAME, SERVER_DIRECTORY, SERVER_BINARY_PATH)


def plugin_loaded():
    server.setup()


def plugin_unloaded():
    server.cleanup()


def is_node_installed():
    return shutil.which('node') is not None


class LspJSONPlugin(LanguageHandler):
    @property
    def name(self) -> str:
        return PACKAGE_NAME.lower()

    @property
    def config(self) -> ClientConfig:
        # Calling setup() also here as this might run before `plugin_loaded`.
        # Will be a no-op if already ran.
        # See https://github.com/sublimelsp/LSP/issues/899
        server.setup()

        settings = sublime.load_settings(SETTINGS_FILENAME)
        client_configuration = settings.get('client')
        default_configuration = {
            "enabled": True,
            "command": ['node', server.binary_path, '--stdio'],
            "languages": [
                {
                    "languageId": "json",
                    "scopes": ["source.json"],
                    "syntaxes": [
                        "Packages/JavaScript/JSON.sublime-syntax",
                        "Packages/JSON/JSON.sublime-syntax"
                    ]
                }
            ]
        }
        default_configuration.update(client_configuration)
        default_configuration['settings']['json']['schemas'] = schemas

        return read_client_config(self.name, default_configuration)

    def on_start(self, window) -> bool:
        if not is_node_installed():
            sublime.status_message('Please install Node.js for the JSON server to work.')
            return False
        return True

    def on_initialized(self, client) -> None:
        pass

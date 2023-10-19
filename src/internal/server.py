#!/usr/bin/env python3

import connexion

import sys
import os

# Get the absolute path to src/internal/api/
module_path = os.path.abspath(os.path.join('src', 'internal', 'api'))

# Add this path to sys.path if it's not already there
if module_path not in sys.path:
    sys.path.append(module_path)

from ..internal.api.server_template import encoder


def main():
    app = connexion.App(__name__, specification_dir='./api/server_template/openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'template backend index service'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()

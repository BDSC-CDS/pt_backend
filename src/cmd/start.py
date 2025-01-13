#!/usr/bin/env python3

import argparse
import connexion
import os
import sys
from flask_cors import CORS


from ..internal.cmd.provider import config
from ..internal.cmd.provider import controllers
from ..internal.cmd.provider import db
from ..internal.api.server_template import encoder
from ..internal.connexion import connexion as connexion_utils
from ..internal.cmd.provider import orphans

def main():    
    run_server()


def run_server():
    p = argparse.ArgumentParser(description="Application settings")
    p.add_argument('--env', type=str, help='Runtime environment, e.g. int, acc, prod...')
    p.add_argument('--config', type=str, help='Config file path', default="./configs/dev/pt_backend.yml")
    args = p.parse_args()

    conf = config.provide_config(args.config)
    d = db.provide_db("pt_backend")
    
    app = connexion.App(__name__, specification_dir='../internal/api/server_template/openapi/')

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': conf.daemon.title},
                pythonic_params=False,
                resolver=connexion_utils.Resolver(controllers=controllers.provide_controllers()))
    
    CORS(app.app)

    # Run orphans
    orphans.provide_orphans()

    app.run(port=conf.daemon.http.port)


if __name__ == '__main__':
    main()
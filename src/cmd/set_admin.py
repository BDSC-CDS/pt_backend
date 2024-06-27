#!/usr/bin/env python3

import argparse
# from src.internal.cmd.provider import provide_config, provide_db, provide
from src.internal.cmd.provider.user import provide_user_store

# ### Allow dynamic import resolution from generated pt backend
# # Get the absolute path to src/internal/api/
# module_path = os.path.abspath(os.path.join('src', 'internal', 'api'))
# # Add this path to sys.path if it's not already there
# if module_path not in sys.path:
#     sys.path.append(module_path)


# from ..internal.cmd.provider import config
# from ..internal.cmd.provider import controllers
# from ..internal.cmd.provider import db
# from ..internal.api.server_template import encoder
# from ..internal.connexion import connexion as connexion_utils

# def main():    
#     run_server()


# def run_server():
#     p = argparse.ArgumentParser(description="Application settings")
#     p.add_argument('--env', type=str, help='Runtime environment, e.g. int, acc, prod...')
#     p.add_argument('--config', type=str, help='Config file path', default="./configs/dev/pt_backend.yml")
#     args = p.parse_args()



p = argparse.ArgumentParser(description="Set Admin")
p.add_argument('--userid', type=int, help='User id')
args = p.parse_args()

store = provide_user_store()
store.set_admin(args.userid)


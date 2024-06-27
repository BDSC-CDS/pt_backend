#!/usr/bin/env python3

import argparse
from src.internal.cmd.provider.user import provide_user_store
from src.internal.cmd.provider.config import provide_config



p = argparse.ArgumentParser(description="Set Admin")
p.add_argument('--userid', type=int, help='User id')
p.add_argument('--config', type=str, help='Config file path', default="")
args = p.parse_args()

if args.config != "":
    provide_config(args.config)

store = provide_user_store()
store.set_admin(args.userid)


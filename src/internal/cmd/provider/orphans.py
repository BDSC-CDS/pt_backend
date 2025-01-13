from src.internal.steward import steward
from src.internal.cmd.provider.steward import provide_steward

orphans = None

def provide_orphans():
    global orphans
    if orphans is not None:
        return orphans

    orphans = {}
    orphans['steward'] = provide_steward()
        
    return orphans
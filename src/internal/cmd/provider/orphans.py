orphans = None

def provide_orphans():
    global orphans
    if orphans is not None:
        return orphans

    orphans = {}
        
    return orphans
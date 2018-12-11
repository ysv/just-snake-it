import sys
# import code
# code.interact(local=dict(globals(), **locals()))

def run_pyit():
    """run pyit"""
    from pyit.run import Run
    from pyit.writers import print_inspection_files
    from pyit.config import Config

    config = Config.with_file()

    try:
        runners = []
        for arg in sys.argv[1:]:
            runners.append(Run(arg))

        if config.value('verbose'):
            print_inspection_files(runners)

    except KeyboardInterrupt:
        sys.exit(1)

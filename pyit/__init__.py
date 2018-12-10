import sys

# from .__pkginfo__ import version as __version__


def run_pyit():
    """run pylint"""
    from pyit.run import Run

    try:
        runners = []
        for arg in sys.argv[1:]:
            runners.append(Run(arg))
            print(runners[-1].inspection_files)

    except KeyboardInterrupt:
        sys.exit(1)

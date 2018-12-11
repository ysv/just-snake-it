def print_inspection_files(runners):
    # TODO: Beautiful output for inspection files.
    print('Files for inspection:')
    for r in runners:
        for f in r.inspection_files:
            print(f)


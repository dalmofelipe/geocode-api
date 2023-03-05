from subprocess import run


def console_run():
    run(['uvicorn', 'geocode.main:api', '--reload'])

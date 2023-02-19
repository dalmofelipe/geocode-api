import subprocess


def console_run():
    subprocess.run(['uvicorn', 'geocode.api.main:api', '--reload'])

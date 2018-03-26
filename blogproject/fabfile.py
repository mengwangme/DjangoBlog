from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/KeepitReal555/DjangoBlog.git"

env.user = 'faiz'
env.password = 'best01892'

env.hosts = ['67.216.221.161']

env.port = '27773'

def deploy():
    source_folder = '/home/faiz/sites/67.216.221.161/DjangoBlog'

    run('cd %s && git pull' % source_folder)

    run("""
        cd {} &&
        /home/faiz/sites/67.216.221.161/env/bin/pip install -r requirements.txt &&
        /home/faiz/sites/67.216.221.161/env/bin/python3 manage.py collectstatic --noinput &&
        /home/faiz/sites/67.216.221.161/env/bin/python3 manage.py migrate
        """.format(source_folder), shell=True)

    sudo('restart 67.216.221.161')
    sudo('service nginx reload')
from os import environ
from batchspawner import SlurmSpawner

c = get_config()  #noqa

c.JupyterHub.bind_url = 'http://:8000/jhub'
c.JupyterHub.base_url = '/jhub'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

c.Authenticator.allowed_users = {'csadmin'}
c.Authenticator.admin_users = {'csadmin'}

c.JupyterHub.spawner_class = SlurmSpawner
c.Spawner.default_url = '/lab'
c.Spawner.http_timeout = 300
c.Spawner.start_timeout = 300
c.Spawner.hub_connect_url = 'http://test.com' # change this value
c.SlurmSpawner.startup_poll_interval = 5

c.SlurmSpawner.batch_script = '''#!/bin/bash
#SBATCH --output={{homedir}}/jupyterhub_slurmspawner_%j.log
#SBATCH --job-name=spawner-jupyterhub
#SBATCH --chdir={{homedir}}
#SBATCH --export={{keepvars}}
#SBATCH --get-user-env=L

docker run --rm --network=host \
        -e JUPYTERHUB_SERVICE_URL \
        -e JUPYTERHUB_API_TOKEN \
        -e JUPYTERHUB_BASE_URL \
        -e JUPYTERHUB_DEFAULT_URL \
        -e JPY_API_TOKEN \
        -e JUPYTERHUB_SERVICE_PREFIX \
        -e JUPYTERHUB_OAUTH_CALLBACK_URL \
        -e JUPYTERHUB_OAUTH_ACCESS_SCOPES \
        -e JUPYTERHUB_COOKIE_HOST_PREFIX_ENABLED \
        -e JUPYTERHUB_API_URL \
        -e JUPYTERHUB_CLIENT_ID \
        -e JUPYTERHUB_OAUTH_SCOPES \
        -e JUPYTERHUB_USER \
        -e JUPYTERHUB_ACTIVITY_URL \
        jhub \
        {{cmd}}
'''

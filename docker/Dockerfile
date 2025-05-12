FROM quay.io/jupyter/docker-stacks-foundation

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    fonts-liberation \
    pandoc \
    run-one && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

WORKDIR /tmp
RUN mamba install --yes \
    'jupyterhub-singleuser' \
    'batchspawner' && \
    jupyter server --generate-config && \
    mamba clean --all -f -y && \
    rm -rf "/home/${NB_USER}/.cache/yarn" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

ENV JUPYTER_PORT=8888
EXPOSE $JUPYTER_PORT

COPY jupyter_server_config.py docker_healthcheck.py /etc/jupyter/

USER root
RUN fix-permissions /etc/jupyter/

HEALTHCHECK --interval=3s --timeout=1s --start-period=3s --retries=3 \
    CMD /etc/jupyter/docker_healthcheck.py || exit 1

USER ${NB_UID}

WORKDIR "${HOME}"

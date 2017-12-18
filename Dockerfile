FROM jupyter/datascience-notebook:033056e6d164  
# If using your own Docker image, use the following `FROM` command syntax substituting your image name

ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini /tini
USER root
RUN chmod +x /tini
USER jovyan

# If using your own Docker image without jupyter installed:
# RUN pip install jupyter

# you can also pass this at runtime
ENV JUPYTER_TOKEN=my_secret_token

EXPOSE 8888
ENTRYPOINT [/tini, --]
# --no-browser & --port aren't strictly necessary. presented here for clarity
CMD [jupyter-notebook, --no-browser, --port=8888]


# if running as root, you need to explicitly allow this:
# CMD [jupyter-notebook, --allow-root, --no-browser, --port=8888]

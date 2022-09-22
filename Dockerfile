FROM pnexuscoe.rjil.ril.com:5115/jioent/health/jio-python-base:3.8-slim

# Build dependencies
RUN apt-get update && apt-get install -y build-essential
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG PROXY_HTTP
ARG PROXY_HTTPS
ARG PROXY_NO
ENV http_proxy $PROXY_HTTP
ENV https_proxy $PROXY_HTTPS
ENV no_proxy $PROXY_NO

# setting up pypy feed
COPY pip_config_file .
ENV PIP_CONFIG_FILE "/usr/src/app/pip_config_file"

# Installing requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV http_proxy ""
ENV https_proxy ""
ENV no_proxy ""
RUN echo $http_proxy
RUN echo $https_proxy
RUN echo $no_proxy

# Adding remaining files
ADD . .

CMD ["python3", "data_service_server.py"]

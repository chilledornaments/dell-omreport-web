# dell-omreport-web

## Overview

I wrote this tool to solve two probles:

- While OMSA is a great tool, I'm not a fan of its clunky, outdated interface.

- I firewall access to OMSA, so you have to establish an SSH tunnel through a bastion to access it. This creates a non-zero amount of work to access the interface.

## Installing the Web Interface and API

- Have a CentOS/RHEL machine

- Clone the repo to `/opt/`

- Edit `/opt/dell-omreport-web/omsa.conf` to reflect your `server_name`

- Edit `/opt/dell-omreport-web/config.py`. More details in the `Config` section

- Run the install script (`rh-install.sh`) as root

*Caveat: * I haven't written an installer for anything that doesn't use YUM

The install script:

- Installs the `epel-release`, `python36`, `python36-devel`, `python36-setuptools`, and `nginx` packages

- Install the packages in Pipfile

- Adds a non-privileged user named `omsa` and changes the ownership of `/opt/dell-omreport-web/` to `omsa`

- Installs `nginx`

- Adds the latest MongoDB repo and installs MongoDB

- Starts and enables MongoDB

    - *Caveat: * You will need to create your own user for Mongo

- Copies the service and NGINX config files to their appropriate locations

- Enables NGINX and omsa-web.

- Restarts NGINX

## Installing the Client Scripts

Great, you have a web interface. Now to get some data.


[This repository](https://github.com/mitchya1/dell-omreport-parser) has the client scripts. Follow the steps in the README.

## Config

`SECRET_KEY`: A secret key that's really long and complicated (i.e. openssl rand -base64 50)

`MONGOALCHEMY_DATABASE`: The Database name. Something like `omsaReports`

`MONGOALCHEMY_SERVER`: The Mongo server (i.e. 127.0.0.1)

`MONGOALCHEMY_USER`: Required if `MONGOALCHEMY_SERVER_AUTH` is True

`MONGOALCHEMY_PASSWORD`: Required if `MONGOALCHEMY_SERVER_AUTH` is True

`MONGOALCHEMY_SERVER_AUTH`: Boolean. If you need to authenticate against MongoDB

`SLACK`: Boolean. Send Slack alerts or not

`SLACK_CHANNEL`: Required if `SLACK` is True. The channel to post messages to

`SLACK_USERNAME`: Required if `SLACK` is True. The username for OMSA to post messages in Slack as

`SLACK_ICON`: Required if `SLACK` is True. The icon to use when posting Slack messages

`SLACK_WEBHOOK`: Required if `SLACK` is True. The incoming Slack webhook


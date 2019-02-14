#!/usr/bin/env bash

if [ "${UID}" != 0 ]
then
echo "Please run as root"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing epel-release"
echo ""
echo "*************************************************************"

if yum -y install epel-release > /dev/null
then
echo "*************************************************************"
echo ""
echo "epel-release installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing epel-release"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing python36 packages"
echo ""
echo "*************************************************************"

if yum -y install python36 python36-devel python36-setuptools > /dev/null
then
echo "*************************************************************"
echo ""
echo "Python installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing Python36"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing pip3"
echo ""
echo "*************************************************************"

if /usr/bin/easy_install-3.6 pip > /dev/null
then
echo "*************************************************************"
echo ""
echo "Pip3 installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing Pip3"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing Python modules"
echo ""
echo "*************************************************************"

if /usr/local/bin/pip3 > /dev/null
then
echo "*************************************************************"
echo ""
echo "Python modules installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing Python modules"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing MongoDB repo"
echo ""
echo "*************************************************************"

cat <<\EOF > /etc/yum.repos.d/mongo-org-4.0.repo
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
EOF

echo "*************************************************************"
echo ""
echo "Updating package cache"
echo ""
echo "*************************************************************"

yum makecache fast > /dev/null

echo "*************************************************************"
echo ""
echo "Installing MongoDB"
echo ""
echo "*************************************************************"

if yum -y install mongodb-org > /dev/null
then
echo "*************************************************************"
echo ""
echo "MongoDB installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing MongoDB"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Starting and enabling MongoDB"
echo ""
echo "*************************************************************"

if systemctl start mongod && systemctl enable mongod > /dev/null
then 
echo "*************************************************************"
echo ""
echo "MongoDB started and enabled"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error starting and enabling MongoDB"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Installing NGINX"
echo ""
echo "*************************************************************"

if yum -y install nginx > /dev/null
then
echo "*************************************************************"
echo ""
echo "NGINX installed"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error installing NGINX"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Starting and enabling NGINX"
echo ""
echo "*************************************************************"

if systemctl start nginx && systemctl enable nginx > /dev/null
then 
echo "*************************************************************"
echo ""
echo "NGINX started and enabled"
echo ""
echo "*************************************************************"
else
echo "*************************************************************"
echo ""
echo "Error starting and enabling NGINX"
echo ""
echo "*************************************************************"
exit 1
fi

echo "*************************************************************"
echo ""
echo "Copying config files"
echo ""
echo "*************************************************************"

cp $PWD/omsa.conf /etc/nginx/conf.d/

cp $PWD/omsa-web.service /etc/systemd/system/

if [ $(getenforce) == "Enforcing" ];
then
restorecon /etc/nginx/conf.d/omsa.conf
restorecon -r /etc/systemd/system/omsa-web.service
fi

echo "*************************************************************"
echo ""
echo "Config files copied"
echo ""
echo "*************************************************************"

echo "*************************************************************"
echo ""
echo "Starting omsa-web"
echo ""
echo "*************************************************************"

systemctl daemon-reload > /dev/null

systemctl start omsa-web > /dev/null

echo "*************************************************************"
echo ""
echo "Allowing NGINX to connect to the network"
echo ""
echo "*************************************************************"

setsebool -P httpd_can_network_connect 1

echo "*************************************************************"
echo ""
echo "Restarting NGINX"
echo ""
echo "*************************************************************"

systemctl restart nginx > /dev/null

echo "*************************************************************"
echo ""
echo "Installation complete!"
echo ""
echo "*************************************************************"

exit 0

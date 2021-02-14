#!/bin/bash

# update
apt update

# install python
# apt install software-properties-common
# add-apt-repository ppa:deadsnakes/ppa
# apt update
# apt install python3.8
echo "Setup Python"
apt-get purge -y python3-pip
apt-get install -y python3-pip
apt-get install -y python3-venv
# python3 -m pip install --user --upgrade pip
# python3 -m pip install --user virtualenv

# install mongodb
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt update
apt install -y mongodb-org
systemctl start mongod
systemctl enable mongod

# prepare python env
cd backend
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
deactivate
cd ..

# install nginx (for frontend and reverse proxy)
apt install nginx -y
ufw allow 'Nginx HTTP'
ufw allow 'OpenSSH'
echo "y" | ufw enable
ufw default deny
systemctl enable nginx

# install node.js using nvm (for frontend build)
bash ./install_nvm.sh
source ~/.profile
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This $nvm install 14.5.0
nvm install 14.5.0

# build the frontend and serve through nginx
chmod -R 755 /var/www/html
cd frontend
npm install
npm run build
rm /var/www/html/index.nginx-debian.html
cp -r ./public/* /var/www/html
cp ./nginx /etc/nginx/sites-available/default
systemctl restart nginx
cd ..

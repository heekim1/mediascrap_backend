#!/bin/bash
cd $HOME
sudo yum install -y bzip2 wget
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -f -p $HOME/miniconda
$HOME/miniconda/bin/conda install -c conda-forge -y awscli
rm Miniconda3-latest-Linux-x86_64.sh
sudo yum update -y
sudo yum install git -y
sudo yum install -y docker
sudo service docker start
sudo chmod 666 /var/run/docker.sock
sudo usermod -a -G docker ec2-user
echo "the userdata_amazon.tpl has benn executed" > /home/ec2-user/userdata_amazon_done.txt

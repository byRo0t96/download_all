#!/bin/bash
# v.0.0.1
# download_all
# Coded by: Ro0t-96
# Github: https://github.com/byRo0t96
printf '\033]2;Download_All\a'
user=$1
git=$2
#########################downloads folder
downloads_folder() {
if [[ -e $user ]]
then
echo "$user folder is exist."
else
echo "mkdir $user folder."
mkdir $user
fi
}
########################down function
down(){
downloads_folder
cd $user
if [[ -e $git ]]
then
echo "$git is exist."
echo "delete $git..."
rm -rf $git
git clone https://github.com/$user/$git.git
else
git clone https://github.com/$user/$git.git
fi
cd ..
}

down

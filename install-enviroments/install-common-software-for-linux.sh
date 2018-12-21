
sudo apt update

# basic
sudo apt install -y git tmux vim lrzsz
echo "set nu" >> ~/.vimrc

# pinyin
sudo add-apt-repository ppa:fcitx-team/nightly
sudo apt update
sudo apt-get install -y fcitx fcitx-config-gtk fcitx-table-all im-switch
# download dpkg from  http://pinyin.sogou.com/linux/?r=pinyin 
# sudo dpkg -i ***.deb

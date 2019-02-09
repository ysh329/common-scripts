# 服务器网络域名无法解析

```shell
sudo rm /etc/resolv.conf
sudo vim /etc/resolv.conf
```

加入如下内容：

```
nameserver 223.5.5.5
nameserver 114.114.114.114
```

参考
- ubuntu域名解析失败解决方案 - 廿四桥明月夜的博客 - CSDN博客  
https://blog.csdn.net/u012207345/article/details/78339218
- ubuntu12.04 apt-get upgrade失败的问题 - andy1219111的专栏 - CSDN博客  
https://blog.csdn.net/andy1219111/article/details/12943699




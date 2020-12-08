查看系统架构

```shell
arch
```

查看系统版本

```shell
cat /etc/redhat-release
```

安装mysql

```shell
yum insatll mysql-community-server
yum insatll *.rpm
```

启动mysql

```shell
systemctl start mysqld.service
```

开机自启mysql

```shell
systemctl enable mysqld
```

查看mysql状态

```shell
systemctl status mysqld.service
rpm -qa |  grep -i 'mysql'
```

 获取mysql密码

```shell
grep 'password' /var/log/mysqld.log | head -1
```

登录mysql

```
mysql -u root -p
```

修改mysql root密码

```mysql
ALRET  USER 'root'@'localhost' IDENTIFIED BY 'new_password'
```

查看mysql密码安全设置

```mysql
SHOW VARIABLES LIKE 'validate_password%'
```

设置密码复杂度

```mysql
set global validate_password_policy=0
```

查看字符集

```mysql
show variables like '%character%';
```

 查看校对规则

```mysql
show variables like '%collation_%';
```




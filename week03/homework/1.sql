#修改字符集

alter database testdb character set utf8mb4;

#验证字符集

show variables like '%character%';


#添加用户

grant all privileges on *.* to 'longpengyu'@'%' identified by 'longpengyu' ;
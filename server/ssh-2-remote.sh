#!/usr/bin/expect -f

set ip 127.0.0.1
set port 4530
set user ysh329
set password 12345678

spawn ssh -p $port $user@$ip -L 9999:$ip:9999

expect {
  "*yes/no" { send "yes\r"; exp_continue}
  "*password:" { send "$password\r" }
}
interact

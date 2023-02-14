## Steps

Generate SSH key pair
```
ssh-keygen -t rsa -f ce -C piyush_dezc_2023 -b 2048
ssh-keygen -t rsa -f ce -C ubuntu -b 2048
```

Connect via ssh
```
ssh -i ce piyush_dezc_2023@35.196.116.33
ssh -i ce ubuntu@34.148.10.17
```

# What is Reflector?


## Warning
Some param will produce lots of bandwidth, use it with care.

## Usage
```bash
cat urls.txt | reflector -a -x $HTTP_PROXY | tee results.txt | notify -silent
```

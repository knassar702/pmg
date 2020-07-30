# pmg
Extract parameters/paths from urls for bug hunting


## usage :
* `$ cat urls.txt | python3 PmG.py`
#### results

<img src='src/image.png'>


here you can add more parameters/paths using regex :D

```python
wordlist = [
        r'(url=|password=|link=|u=|username=|link_id=)',
        '/+CSCOU+', # CVE-2020-3452
        r'\.(sql|db|tar|backup|bak|zip|git|php)'
        ]
```


# pmg
Extract parameters/paths from urls


## usage :
* `$ cat urls.txt | python3 PmG.py`
#### results

<img src='src/image.png'>


* Save results
 `$ cat urls.txt | python3 PmG.py ResultsFile.txt`

here you can add more parameters/paths using regex :D

```python
wordlist = [
        r'(url=|password=|link=|u=|username=|link_id=)',
        '/+CSCOU+', # CVE-2020-3452
        r'\.(sql|db|tar|backup|bak|zip|git|php)'
        ]
```


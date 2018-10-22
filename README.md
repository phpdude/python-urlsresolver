# urlsresolver v1.2.0
Python urls resolver library with meta refresh support.

You can expand real address of any shortened url with `urlsresolver.resolve_url(url)` function.

Checks for meta refresh html tags & refresh http header. 

# Installation

You can install library as usual with `pip install urlsresolver`.
 
# Python module usage

Example of usage module as console utility.

```
@dude > python -m urlsresolver http://t.co/dRW1iSInvA -V
Source:
    http://t.co/dRW1iSInvA

Expanded:
    http://www.findelight.net/frenbull_detail.html?id=1078982008178233213_2206075018

Redirects history:
    1. http://t.co/dRW1iSInvA
    2. http://www.findelight.net/frenbull_detail.html?id=1078982008178233213_2206075018

Total 1 redirects
```

# Contributon and contacts

You can write me to alexandr.shurigin@gmail.com for any question.

Pull Requests are welcome.

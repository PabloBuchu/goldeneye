QUICKSTART
==========

Just do it!
```
python setup.py install
```
or for dynamic linking
```
python setup.py develop
```

You can wrap your WSGI app with `goldeneye.MMetricsMiddleware` to auto serve prometheus metrics under `/metrics`


#!/usr/bin/env python3
import os
import http.cookies
count = 0
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")
if name:
    count = int(name.value) + 1
print("Content-type: text/html\n")
print("Set-cookie: name={}" .format(count))

print(count)
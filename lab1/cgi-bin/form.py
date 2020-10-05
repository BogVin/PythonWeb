#!/usr/bin/env python3
import cgi
import os
import http.cookies
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
if cookie.get("counter"):
    visitor_counter = cookie.get("counter").value
    visitor_counter = int(visitor_counter) + 1 if visitor_counter else 0
    print(f"Set-Cookie: counter={visitor_counter}")
else:
    visitor_counter = 1
    print(f"Set-Cookie: counter={visitor_counter}")

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")

option = form.getvalue("option","не задано")


radio = form.getvalue("dzen")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Ім'я: {}</p>".format(text1))
print("<p>Прізвище: {}</p>".format(text2))

print("<p>Музика:</p>")
for elem in option:
    print("<p>{}</p>".format(elem))

print("<p>Любимий богатир: {}</p>".format(radio))



print("""</body>
        </html>""")

print("Надісланих форм", visitor_counter)

import math
import os
import re
import sys

from flask import Flask, Response, request

# Allow very large numbers to be converted to strings (Python 3.11+ limit)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

# Set your email here or via the EMAIL environment variable
EMAIL = os.environ.get("EMAIL", "alibekaubakir555@gmail.com")
ROUTE = "/" + re.sub(r"[^A-Za-z0-9]", "_", EMAIL)

app = Flask(__name__)
DIGITS = re.compile(r"[0-9]+")


def parse(value):
    """Return int if value is a non-negative integer string, else None."""
    if value is None or not DIGITS.fullmatch(value):
        return None
    return int(value)


@app.get(ROUTE)
def lcm():
    x = parse(request.args.get("x"))
    y = parse(request.args.get("y"))
    body = "NaN" if x is None or y is None else str(math.lcm(x, y))
    return Response(body, mimetype="text/plain")


@app.get("/")
def health():
    return Response("ok", mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

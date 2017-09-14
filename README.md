# imstillalive.xyz

I'm Still Alive - Uptime/Pinger thing for .. whatever


# Quickstart

There's one generic endpoint, which takes the form:

`http://imstillalive.xyz/ping/<thing>`

## Ping via PUT

To ping with the name of a `thing`, as if to say "I'm alive!", issue a PUT request

    curl -X PUT "http://imstillalive.xyz/ping/foo"

## Check via GET

To see if a `thing` has pinged in the last N seconds (currently N=1200, or 20 min), issue a GET request

    curl -X GET "http://imstillalive.xyz/ping/foo"

If the `thing` has pinged in the last N seconds, this will return a 200.

If the `thing` is unknown, or the time window is up, it will return a 404

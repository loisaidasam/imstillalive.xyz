# imstillalive.xyz
I'm Still Alive - Uptime/Pinger thing for .. whatever


# Quickstart

## It's a two step process:

### 1. Ping with name of thing

    curl http://imstillalive.xyz/ping/foo

### 2. Check to see if thing happened in the last N seconds (currently set to 1200, 20 min)

    curl http://imstillalive.xyz/check/foo

This will return a 200 and how many seconds have elapsed, or 404 if the time window is up.

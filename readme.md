# Prices Server

Scripts to fetch price info and serve it to the Sumero UI. This is expected to be run on a Linux machine running apache, with a cron job calling the `fetch_and_store.sh` script regularly. The server should run on the same domain as the interface is served from, and have a regular, non-open CORS policy.

`config.json` contains a list of the price identifiers to fetch. This should be updated whenever the interface needs to use a new price identifier.

The script writes price info to `/var/www/htlm/prices.json`, which the interface is expected to fetch as needed.

It expects a file `key` containing an api key for the cryptowatch price platform.

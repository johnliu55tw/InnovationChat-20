# Innovation Chat #20
**KKBOX Open API Workshop : 帶你翻玩 KKBOX Open API．快速打造音樂應用 MVP！**

## Demo code

This repository contains the sample code for Innovation Chat #20 Workshop:

* playlist\_search

## Getting started

The required environment for running the sample codes is managed by `pipenv`.

First, you have to install `pipenv` (See [https://docs.pipenv.org](https://docs.pipenv.org) for more information.)

```
$ pip install pipenv
```

Then, clone this project and change the `KKBOX_CLIENT_ID` and `KKBOX_CLIENT_SECRET` of the file
`demo-code/playlist_search/playlist_search/playlist_search.py`, with your client ID and client secret.
If you don't know what the client ID and secret are, please visit [KKBOX Developer Site](https://developer.kkbox.com/#/).

Finally, start the web app with `pipenv`:
```
$ pipenv run python3 demo-code/playlist_search/playlist_search/playlist_search.py
```

You should see something like:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 329-125-323
```

Now the web app is up and running. Visit [http://localhost:5000](http://localhost:5000) to test it.

## Resources

* [KKBOX Developer Site](https://developer.kkbox.com)
* [Innovation Chat #20 Slides](https://slides.com/johnliu55tw/python-x-kkbox-open-api)

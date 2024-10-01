# ![RealWorld Example App](logo.png)

> ### Express.js + MongoDB + JavaScript codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.


### [Demo](https://demo.realworld.io/)&nbsp;&nbsp;&nbsp;&nbsp;[RealWorld](https://github.com/gothinkster/realworld)


This codebase was created to demonstrate a fully fledged fullstack application built with **Express.js + MongoDB + JavaScript** including CRUD operations, authentication, routing, pagination, and more.

We've gone to great lengths to adhere to the **Express.js + MongoDB + JavaScript** community styleguides & best practices.

For more information on how to this works with other frontends/backends, head over to the [RealWorld](https://github.com/gothinkster/realworld) repo.

# Getting started

1. install npm
1. make sure mongo is running
1. define needed env vars
   - `DATABASE_URI` - the uri to the mongo database: mongodb://127.0.0.1:27017/somedbname (assuming mongo is running on localhost:27017)
   - `ACCESS_TOKEN_SECRET` - the secret used for the JWT
1. execute `node api/index.js`
   - e.g., `ACCESS_TOKEN_SECRET=xyzzy-plover-boom DATABASE_URI=mongodb://127.0.0.1:27017/somedb node api/index.js`

## Contrast-specific

1. A contrast_security.yaml config file should be present and configured appropriately.
1. The contrast agent should be installed as a dependency.
    1. For developmental testing, linking to the local node-mono repo is useful.
1. To enable perf use a command line like: `CSI_PERF_INTERVAL=10000 CSI_PERF=1 ACCESS_TOKEN_SECRET=xyzzy-plover-boom DATABASE_URI=mongodb://127.0.0.1:27017/somedb node --import @contrast/agent api/index.js`
    1. loads the agent with perf enabled, using a 10 second interval for writing the log.
1. set up `locust` per instructions in the `script-locust/README.md`
1. run the request-generating script, `script-locust/locustfile.py` using `locust -f locust-script/locustfile.py --headless -i 1`.
    1. `--headless` just means don't use the web UI, i.e., pure command line
    1. `-f` specifies the file (more TBD, exercising different aspects of the code)
    1. `-i 1` specifies 1 iteration.
1. the agent writes `agent-perf.jsonl`
    1. `agent-perf.jsonl` can be analyzed using tools in `script-analysis/`.

# How it works

> All the routes are defined in the `src/routes` folder, and their corresponding controllers are implemented in the `src/controllers` folder.

# Design Choices and Tradeoffs

- Only one `access_token_secret` is used for all the accounts registration and login. Drawback: data can be forged if this secret is leaked
- Included array structures, e.g. list of comments in the article model and favorited articles in the user model. Drawback: not good for scalability
- Usernames are case-sensitive

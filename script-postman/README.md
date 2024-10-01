# RealWorld API Spec

## Running API tests locally

First, make sure the realWorld-server is running per instructions in the main README.

To locally run the provided Postman collection against Contrast-Security-OSS/realWorld-server, execute:

```
APIURL=http://localhost:4000/api ./run-api-tests.sh
```

N.B. The username needs to be unique each run to prevent failures due to duplicate usernames. Most tests will run, but it's not ideal.

```
APIURL=http://127.0.0.1:4000/api USERNAME=brucexyzzy7 ./api/run-api-tests.sh
```

For more details, see [`run-api-tests.sh`](run-api-tests.sh).


## Thoughts on more sustained testing

10 minute run?

Create users, wait (mark?)

Run PM collection tests, but
- multiple users concurrently
  - 1, 10, ???
- predefined test data
  - safe/unsafe
  - varied sizes
- random test data?
  - safe/unsafe
  - varied sizes 10, 100, 1000, 10000
- timing
  - immediate
  - think time


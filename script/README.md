# RealWorld API Spec

## Running API tests locally

To locally run the provided Postman collection against Contrast-Security-OSS/realWorld-server, execute:

```
APIURL=http://localhost:4000/api ./run-api-tests.sh
```

N.B. The username needs to be unique each run to prevent failures due to duplicate usernames. Most tests will run, but it's not ideal.

```
APIURL=http://127.0.0.1:4000/api USERNAME=brucexyzzy7 ./api/run-api-tests.sh
```

For more details, see [`run-api-tests.sh`](run-api-tests.sh).

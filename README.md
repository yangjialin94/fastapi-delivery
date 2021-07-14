# fastapi_delivery

Delivery API implemented with FastAPI.

## Development

### How to start and stop the applicaton

Run these commands in this directory

```
$ docker-compose -f docker-compose.dev.yml up --build --force-recreate --remove-orphans
$ docker-compose -f docker-compose.dev.yml down -v
```

Navigate to http://0.0.0.0:8081/docs/

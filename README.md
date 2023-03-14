# docker-neptune

Imitate aws neptune for local dev

## Usage
```console
docker build -t neptune .
docker run --rm -p 8182:8182 neptune

curl "localhost:8182/gremlin?gremlin=g.V()"
```

# Flask DB migration POC

![fisdom logo][fisdom-logo]

## Dependencies

| Tool | Link |
| ------ | ------ |
| docker | <https://docs.docker.com/engine/install/ubuntu/> |
| docker-compose | <https://docs.docker.com/compose/install/> |

## Build application

```sh
~$ docker-compose build
```

## Run application

```sh
~$ docker-compose up -d
```

## Build and run application

```sh
~$ docker-compose up --build -d
```

## Localhost URL

```sh
http://localhost:5000
```

## Setup Initial DB

```sh
~$ flask db init
```

## Create DB migrations

```sh
~$ flask db migrate
```

## Migrate DB

```sh
~$ flask db upgrade
```

## Docker based Setup just restart container to apply migrations

```sh
~$ docker-compose restart flask
```

[fisdom-logo]: <https://my.fisdom.com/static/img/plutus-finwizard.png>

# Docker

Docker is a tool to create images that represent isolated and reproducible environments. These images can be run as containers.

Docker uses a so-called layered file system which enables the containers to share common parts and the end result is that containers are way less of resource-hog on the host system than a virtual machine.

## Docker vs VM

Docker containers are process isolated.

If you need to run an isolated OS, then you run a VM. If you need to run an isolated app, then you run a container.

Docker is a tool to isolate applications running on one same system, so they don't see the main system and the main system doesn't see the apps.

Docker containers scale better.

VMs can run a different kernel than the one of the host OS.

![](docker-vs-vm.png)

## Layers

A docker image is a set of layers. Each layer is a set of files and directories. Each layer is read-only.

When you run a container, a new layer is created on top of the image. This layer is read-write. It is called the container layer.

A layer can be used by multiple images using the docker cache.

Each time you run a command in the Dockerfile (COPY, RUN, etc.), a new layer is created.

## Dockerfile

A Dockerfile is a text file that contains all the commands a user could call on the command line to assemble an image, image that can be run as a container.

A Dockerfile is a recipe for creating Docker images:

- we start from a base image. This base image can be a minimal Linux distribution, or a Linux distribution with some software already installed, or a Linux distribution with a full-blown application already installed.
- we then run some commands to install software, dependencies, copy files, etc.
- we open some ports so that the container can be accessed from the outside world (if needed).
- finally, we then define what command should be run when the container is started.

### Instructions

#### FROM

The `FROM` instruction sets the Base Image for subsequent instructions. As such, a valid Dockerfile must have `FROM` as its first instruction.

`FROM` can appear multiple times within a single Dockerfile in order to create multiple images.

```dockerfile
FROM <image> [AS <name>]  # we usually name the first image "base"

# do stuff for setting up the app

FROM <image> [AS <name>]  # you can name the second image "app".
```

The base image is pulled from Docker Hub or a private registry if it is not already present on the local host.

FROM can appear multiple times within a single Dockerfile to create multiple images or use one build stage as a dependency for another. Simply make a note of the last image ID output by the commit before each new FROM instruction. Each FROM instruction clears any state created by previous instructions.

#### WORKDIR

The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the Dockerfile.

#### COPY

The `COPY` instruction copies new files or directories from `<src>` and adds them to the filesystem of the container at the path `<dest>`.

#### ADD

`ADD` is similar to `COPY`, but it can also download files from the internet and extract tar files.

#### EXPOSE

The `EXPOSE` instruction informs Docker that the container listens on the specified network ports at runtime.

#### ENV

The `ENV` instruction sets the environment variable `<key>` to the value `<value>`. This value will be in the environment of all "descendant" Dockerfile commands and can be replaced inline in many as well.

```dockerfile
ENV PORT=3000

EXPOSE $PORT

CMD ["python", "app.py", "--port", "$PORT"]  # $PORT will be replaced by 3000
```

#### RUN

We use the `RUN` instruction to execute a command in the container. Like `RUN apt-get install -y python3`, or `RUN pip install -r requirements.txt`.

#### ENTRYPOINT

The `ENTRYPOINT` instruction allows you to configure a container that will run as an executable.

Whatever is set in `ENTRYPOINT` will be executed when the container starts.

#### CMD

The `CMD` instruction should be used to run the app(s) that your container should run, along with any arguments. `CMD` should almost always be used in the form of `CMD ["executable", "param1", "param2"]`.

The `CMD` specifies arguments that will be fed to the ENTRYPOINT.

Quite often, you will see `CMD` in the form of `CMD ["executable", "param1", "param2"]`. This is the preferred form of running a command in a container because it's easy to ovverride the command when debugging.

Whatever is set in `CMD` can be overridden by passing arguments to the `docker run` command.

#### ARG

The `ARG` instruction defines a variable that users can pass at build-time to the builder with the docker build command using the `--build-arg <varname>=<value>` flag.

```dockerfile
ARG VERSION=latest
FROM busybox:$VERSION
```

The code above will use the value of the `VERSION` argument as the tag for the `busybox` image.

#### USER

The `USER` instruction sets the user name or UID to use when running the image and for any `RUN`, `CMD` and `ENTRYPOINT` instructions that follow it in the Dockerfile.

It's good practise to define a user with the lowest possible privileges. By default, Docker runs container as root which inside the container is the root user.

### Dockerfile good practices

Use a `.dockerignore` file to exclude files and directories from the context. The context is the set of files and directories that are sent to the Docker daemon when building an image.

Use `COPY` instead of `ADD` to copy files and directories from the context to the image. `ADD` can also download files from the internet and extract tar files, which is not needed most of the time.

Don't abuse `RUN`:

- Use `RUN` only when you need to install something. If you need to run a command, use `CMD` or `ENTRYPOINT`. `RUN` creates a new layer in the image, which increases the size of the image. `CMD` and `ENTRYPOINT` don't create new layers.
- Each execution of a RUN command creates a temporary container from the last resulting image, executes your commands, and saves the result as a new layer.
- Minimizing RUN commands both reduces the amount of overhead from these intermediate containers, but can also dramatically shrink the size of the resulting image.
- If, for example, you do 2 run commands, one that downloads 1 gig of data, and a second that deletes that gig of data, your resulting image will exceed one gig even though it's not visible in the running container.
- Therefore, when doing large downloads of cached files to do an install or build of an app and you cleanup that build environment when finished, it's a good practice to do that as a single step so the deleted files never make it into any part of the image.

Split long or complex `RUN` statements on multiple lines separated with backslashes to make your Dockerfile more readable, understandable, and maintainable.

Always combine `RUN` `apt-get update` with `apt-get install` in the same RUN statement. If you don’t do this, Docker will cache the `apt-get update` step and you’ll end up with outdated packages in your container.

```dockerfile
FROM ubuntu:18.04
RUN apt-get update  # this will be cached.
RUN apt-get install -y curl  # if we add a new package here, it will use the cached apt-get update. So we might end up with outdated packages.
```

It's best to put layers that are likely to change often at the bottom of the Dockerfile, and layers that change less frequently at the top. This is because Docker uses a layered file system, and each layer is cached. If you change a layer, all the layers coming after will be invalidated. The dockerfile below is bad, because by changing the code (step 3/4), docker will rebuild the pip install step, which might take a while...

```dockerfile
FROM python:3.7                      # Step 1/4
WORKDIR /app                         # Step 2/4
COPY ./src /app                      # Step 3/4
RUN pip install -r requirements.txt  # Step 4/4
```

Instead, we should put the code at the bottom:

```dockerfile
FROM python:3.7
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt  # this step takes time, but the requirements.txt file doesn't change often, so it's ok.
COPY ./src /app  # only this step will be invalidated when changing the code
CMD ["python", "app.py"]
```

The last instruction in the Dockerfile should be `CMD` or `ENTRYPOINT`. This is because the last instruction is the one that will be executed when the container starts. If you put `RUN` as the last instruction, it will be executed when the image is built, not when the container starts.

The last layer should be the app code. This is because the last layer will be the one ran by default.

Set a non-root user. This is for security reasons. If you don't set a non-root user, the container will run as root, which is not recommended.

Empty the caches in the same layer: pip cache (`--no-cache-dir`), apt cache, apk cache, etc.

Disable the virtual environments (poetry, pipenv, etc.). This is because the container is already an isolated environment, so you don't need another isolated environment inside it. `RUN poetry config virtualenvs.create false`

Use `ENV LANG=C.UTF-8` to set the locale to UTF-8. This tells the environment to use UTF-8 encoding by default.

### Multistage builds

In the dockerfile below, we install some systemp dependencies that are only use for installing pip dependencies. The system dependencies are not needed for running the app. So we can use multistage builds to create a smaller image.

```dockefile
# Inherit from Linux Alpine with Python3.7 installed.
FROM python:3.7-alpine AS builder

WORKDIR /app

# Install System dependencies
RUN apk update && apk add --no-cache jpeg-dev zlib-dev python-dev build-base

# Install Python dependencies
RUN pip install --prefix=/install -Ur requirements.txt

# Start a new image.
FROM python:3.7-alpine

WORKDIR /app

# Copy the dependencies
COPY --from=builder /install /install

# Copy local application into image.
COPY ./app.py /app/
```

This is a 2 stage build as you can see separated by the FROM steps written in the Dockerfile.

- Stage 1 install the system dependencies required for us to install our pip dependencies. We use the --prefix option to define a unique path where we want pip to install the packages into.
- Stage 2 starts from a brand new alpine image and instead of installing any system dependencis, we use the COPY command to copy the pip packages installed in /install from our first builder image, into our newly created image.

## Build the image

```bash
docker build -t <image-name>:<tag> <path-to-dockerfile>
```

`-t` is for tagging the image.

When building, docker will show `removing intermediate container` messages. These are the temporary containers that are created for each instruction in the Dockerfile. They are removed after the instruction is executed.

The last layer is tagged with the image name and tag.

Use `--no-cache` to not use the cache when building the image.

## Create a container from the image

```bash
docker run -it --rm -p 8000:3000 <image-name>:<tag>
```

`-it` is for interactive mode.

`--rm` is for removing the container after it exits.

`-p` is for port mapping. The container port 3000 is mapped to the host port 8000. It means that the app inside the container should be listening on port 3000.

You can use `-d` to run the container in detached mode. It means that the container will run in the background and you can continue using the terminal or close it.

## Useful commands

```bash
docker build -t <image-name>:<tag> <path-to-dockerfile>  # build an image
docker images  # list all images
docker rmi <image-id>  # remove an image

docker run -it --rm -p 8000:3000 --name my_container <image-name>:<tag>  # create a container from an image
docker ps  # list all running containers
docker ps -a  # list all containers
docker exec -it <container-id> bash  # run a bash shell inside a container running. It is useful for debugging.
docker start <container-id>  # start a container. It is different from run because it starts a container that was stopped, while run creates a new container. If you used --rm when running the container, you can't start it again since it was removed.
docker stop <container-id>  # stop a container
docker kill <container-id>  # kill a container. It is different from stop because it kills the container immediately, while stop sends a SIGTERM signal to the container, which gives it time to clean up before exiting.
docker logs <container-id>  # show the logs of a container
docker rm <container-id>  # remove a container

# To remove all containers and images:
docker stop $(docker ps -aq) && \  # list and stop all containers
docker rm $(docker ps -aq) && \  # remove all stopped containers
docker builder prune -af && \  # remove all dangling build cache
docker image prune -af && \  # remove all dangling images
docker system prune -af  # remove all stopped containers, all dangling images, all volumes, all networks
```

## Developing with Docker

When developing with Docker, you usually want to update the code inside the container without having to rebuild the image. To do that, you can use volumes.

You can create them in the Dockerfile:

```dockerfile
VOLUME /app  # you can specify only the destination of a volume inside a container
```

Or you can create them when running the container:

```bash
docker run -it --rm -p 8000:3000 -v $(pwd):/app <image-name>:<tag>
```

`-v` is for volume mapping. It maps the current directory to the `/app` directory inside the container.

## Docker compose

Docker Compose is a way to create reproducible Docker containers using a config file instead of extremely long Docker commands. By using a structured config file, mistakes are easier to pick up and container interactions are easier to define.

Docker compose is also a tool to run multiple containers at once. It is configured with a YAML file called `docker-compose.yml`.

Bascially, docker compose will do the "create image" and "create container" steps for you.

```yaml
version: "3.8"  # version of docker compose
services:
  my_app:
    build:
      context: .  # build the image from the Dockerfile in the current directory
    ports:
      - "8000:3000"  # map the container port 3000 to the host port 8000
    environment:
      - PORT=3000  # set the environment variable PORT to 3000
      - DB_HOST=some_db  # set the environment variable DB_HOST to db (not localhost or 0.0.0.0!)

  some_other_service:
    command: python app.py  # run the command "python app.py" when the container starts. This overrides the CMD instruction in the Dockerfile.
    depends_on: db  # wait for the db service to be ready before starting this service

  some_db:
    image: mysql
```

Then you can build and run the container with:

```bash
docker compose up  # build the image and run the container
docker compose down  # stop and remove the container
```

If you need to rebuild the image, you can use:

```bash
docker compose up --build  # build the image
docker compose build --no-cache  # build the image without using the cache
```

During development, you can also map volumes:

```yaml
volumes:
  - ./scripts:/scripts
  - ./files:/files
```

You can easily use pre-existing containers using docker compose:

```bash
docker compose run --rm --name postgres_test_db_container -p 5432:5432 postgres_test_db  # run the postgres container
psql postgresql://postgres:postgres@localhost:5432/postgres  # connect to the postgres container
```

### compose up vs compose run

The command passed by `run` overrides the command defined in the service configuration. The second difference is the `docker compose run` command does not create any of the ports specified in the service configuration.

Prefer use `docker compose up` for running the app and `docker compose run` for running one-off commands.

## Tools

- [Deepo](https://github.com/ufoym/deepo/): Set up deep learning environment in a single command line

## More

- [A Beginner-Friendly Introduction to Containers, VMs and Docker](https://www.freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b/)
- [https://docker-curriculum.com/](https://docker-curriculum.com/)
- Learn Enough Docker to be Useful
  - [Part 1](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b7ba70caeb4b)
  - [Part 2](https://towardsdatascience.com/learn-enough-docker-to-be-useful-1c40ea269fa8)
  - [Part 3](https://towardsdatascience.com/learn-enough-docker-to-be-useful-b0b44222eef5)
  - [Part 4](https://towardsdatascience.com/slimming-down-your-docker-images-275f0ca9337e)
  - [Part 5](https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421)
  - [Part 6](https://towardsdatascience.com/pump-up-the-volumes-data-in-docker-a21950a8cd8)
- <https://towardsdatascience.com/how-docker-can-help-you-become-a-more-effective-data-scientist-7fc048ef91d5>
- <https://training.play-with-docker.com/>
- <https://ikhlestov.github.io/pages/tools/docker/>
- <https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165>
- <http://web.archive.org/web/20201203013356/https://lbartnicki92.github.io/posts/docker-build-from-dockerfile/>
- Tutorial: <https://adamtheautomator.com/docker-compose-tutorial/>
- Debugger in docker: <https://rednafi.com/python/debug_dockerized_apps_in_vscode/>

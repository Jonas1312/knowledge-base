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

#### CMD

The `CMD` instruction should be used to run the software contained by your image, along with any arguments. `CMD` should almost always be used in the form of `CMD ["executable", "param1", "param2"]`.

The `CMD` specifies arguments that will be fed to the ENTRYPOINT.

### Dockerfile good practices

- Use a `.dockerignore` file to exclude files and directories from the context. The context is the set of files and directories that are sent to the Docker daemon when building an image.
- Use `COPY` instead of `ADD` to copy files and directories from the context to the image. `ADD` can also download files from the internet and extract tar files, which is not needed most of the time.
- Don't abuse `RUN`.
  - Use `RUN` only when you need to install something. If you need to run a command, use `CMD` or `ENTRYPOINT`. `RUN` creates a new layer in the image, which increases the size of the image. `CMD` and `ENTRYPOINT` don't create new layers.
  - Each execution of a RUN command creates a temporary container from the last resulting image, executes your commands, and saves the result as a new layer.
  - Minimizing RUN commands both reduces the amount of overhead from these intermediate containers, but can also dramatically shrink the size of the resulting image.
  - If, for example, you do 2 run commands, one that downloads 1 gig of data, and a second that deletes that gig of data, your resulting image will exceed one gig even though it's not visible in the running container.
  - Therefore, when doing large downloads of cached files to do an install or build of an app and you cleanup that build environment when finished, it's a good practice to do that as a single step so the deleted files never make it into any part of the image.
- Split long or complex `RUN` statements on multiple lines separated with backslashes to make your Dockerfile more readable, understandable, and maintainable.
- Always combine `RUN` `apt-get update` with `apt-get install` in the same RUN statement. If you don’t do this, Docker will cache the `apt-get update` step and you’ll end up with outdated packages in your container.

  ```dockerfile
  FROM ubuntu:18.04
  RUN apt-get update  # this will be cached.
  RUN apt-get install -y curl  # if we add a new package here, it will use the cached apt-get update.
  ```

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

docker run -it --rm -p 8000:3000 --name my_container <image-name>:<tag>  # create a container
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
  some-service:
    depends_on: db  # wait for the db service to be ready before starting this service
  db:
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
- <https://lbartnicki92.github.io/posts/docker-build-from-dockerfile/>
Tutorial: <https://adamtheautomator.com/docker-compose-tutorial/>

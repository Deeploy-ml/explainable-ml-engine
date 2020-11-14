# base image
FROM node:12.2.0

# Default value; will be overridden by build_args, if passed
ARG node_env=production

ENV NODE_ENV $node_env

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm install

# add app
COPY . /app

EXPOSE 4200

# start app
CMD ng serve --host 0.0.0.0

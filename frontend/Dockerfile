# syntax=docker/dockerfile:1.4

FROM node:18.10.0 as builder

RUN mkdir /project
WORKDIR /project

RUN npm install -g @angular/cli@13

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200", "--disable-host-check"]
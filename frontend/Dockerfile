# syntax=docker/dockerfile:1.4
FROM node:18.10.0 as build

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app

ARG configuration=production

RUN npm run build -- --output-path=./dist/out --configuration $configuration

FROM nginx

COPY --from=build /app/dist/out /usr/share/nginx/html

COPY /nginx-custom.conf /etc/nginx/conf.d/default.conf


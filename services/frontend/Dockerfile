FROM node:lts-alpine

RUN mkdir app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json .
RUN npm install

COPY src/ ./src/
COPY public/ ./public/
COPY jsconfig.json .
COPY babel.config.js .
COPY vue.config.js .

CMD ["npm", "run", "serve"]
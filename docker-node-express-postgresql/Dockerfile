FROM node:16

RUN apt-get update && apt-get install htop

# Create app directory
WORKDIR /usr/src/node-server

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package.json /usr/src/node-server
# COPY package-lock.json /usr/src/node-server

RUN npm install --silent --progress=false
# If you are building your code for production
RUN npm ci --only=production

# Bundle app source
COPY . .

CMD [ "npm", "run", "start" ]

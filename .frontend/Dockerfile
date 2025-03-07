FROM node:20-alpine as build

WORKDIR /app

# Set the memory limit for Node.js
ENV NODE_OPTIONS=${NODE_OPTIONS:-"--max_old_space_size=512"}

# Install dependencies
COPY package.json package-lock.* ./
RUN npm install

# Build the application
COPY . .
RUN npm run build

# ====================================
FROM build as release

# Ensure the memory limit is set in the release stage as well
ENV NODE_OPTIONS=${NODE_OPTIONS:-"--max_old_space_size=512"}

CMD ["npm", "run", "start"]
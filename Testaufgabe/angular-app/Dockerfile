# Stage 1: Build the Angular application
FROM node:20.15.1 AS build 

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular application
RUN npm run build 

# Stage 2: Serve the Angular application using Nginx
FROM nginx:alpine

# Copy custom Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf 

# Copy the build output to replace the default Nginx contents
COPY --from=build /app/dist/angular-app /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

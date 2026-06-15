# Use an official Nginx image as the base
FROM nginx:stable-alpine

# Set the working directory inside the container to /usr/share/nginx/html, 
# which is the default location for Nginx static content.
WORKDIR /usr/share/nginx/html

# Copy the built static files from the host machine into the container's web root.
# Assuming your build process outputs assets to a 'dist' or similar directory.
COPY ./build/ /usr/share/nginx/html/

# Expose port 80, which is the default HTTP port for Nginx
EXPOSE 80

# The default command to start Nginx is already present in the base image, 
# so no CMD is strictly necessary unless custom configuration is needed.
# CMD ["nginx", "-g", "daemon off;"]
# Use the latest version of the official Nginx image as the base image
FROM nginx:latest

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Add the custom Nginx configuration file from the local directory to the container's file system
ADD default.conf /etc/nginx/conf.d/default.conf

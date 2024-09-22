FROM nginx:alpine
COPY nginx/webroot /webroot
COPY nginx/site.conf /etc/nginx/conf.d/default.conf
RUN chmod o+r,o+x -R /webroot
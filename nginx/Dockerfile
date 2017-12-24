FROM nginx:1

EXPOSE 8080

COPY /nginx.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf
ENTRYPOINT ["/etc/init.d/nginx", "restart"]
CMD ["/bin/bash"]
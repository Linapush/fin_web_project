FROM nginx:1.25.3-alpine

# используем собственный файл конфигурации
RUN rm /etc/nginx/conf.d/default.conf

# копируем файлы из локального репозитория в образ Docker
# /etc/nginx/conf.d стандартный каталог, где Nginx ищет конфигурационные файлы
COPY nginx/nginx.conf /etc/nginx/conf.d

# Nginx будет работать на переднем плане, а не как фоновый процесс
CMD ["nginx", "-g", "daemon off;"]

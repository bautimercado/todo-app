# Usar la imagen oficial de Node.js
FROM node:18-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

# Construir la aplicación
RUN npm run build

# Servir la aplicación usando un servidor web (como nginx)
FROM nginx:alpine

# Copiar los archivos de compilación al servidor web
COPY --from=0 /app/dist /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# No es necesario un CMD, nginx se ejecuta por defecto

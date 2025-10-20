FROM node:20-alpine

WORKDIR /app

# Copiamos solo los archivos necesarios para instalar dependencias
COPY frontend/package*.json ./
RUN npm install

# Copiamos todo el frontend
COPY frontend/ .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
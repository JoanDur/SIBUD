# Usar una imagen base ligera de Java 17
FROM openjdk:17-jdk-slim

# Establecer la zona horaria para evitar problemas con fechas
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar el archivo JAR generado y renombrarlo a backendjava.jar
COPY target/*.jar backendjava.jar

# Exponer el puerto en el que corre la API
EXPOSE 8080

# Usar un ENTRYPOINT para iniciar el servicio
ENTRYPOINT ["java", "-jar", "backendjava.jar"]
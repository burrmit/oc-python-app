####
# This Dockerfile is used in order to build a container that runs the Spring Boot application
#
# Build the image with:
#
# docker build -f docker/Dockerfile -t python/sample-basic .
#
# Then run the container using:
#
# docker run -i --rm -p 8081:8081 python/sample-basic
# syntax=docker/dockerfile:1

FROM ubi8/python-39

WORKDIR /app

# Add application sources with correct permissions for OpenShift
USER 0
COPY . .
RUN chown -R 1001:0 ./
USER 1001

RUN python3 -m venv venv
RUN . venv/bin/activate

# optimize image caching
RUN pip3 install Flask

EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
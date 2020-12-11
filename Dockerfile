FROM python:3.7-slim AS build-python-env
ADD server.py /app
ADD searcher /app
ADD requirements.txt /tmp
WORKDIR /app
RUN pip install --target=/app --no-cache-dir -r /tmp/requirements.txt

FROM node:10.23-slim AS build-nodejs-env
ADD public /app
ADD src /app
ADD package.json /app
WORKDIR /app
RUN npm install && npm run build

FROM gcr.io/distroless/python3-debian10
COPY --from=build-python-env /app /app
COPY --from=build-nodejs-env /app/dist /app/dist
WORKDIR /app

ENV PORT 8080

CMD ["server.py"]
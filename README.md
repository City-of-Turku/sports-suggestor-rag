# Sports suggestor RAG app

This is a [LlamaIndex](https://www.llamaindex.ai/) project using [FastAPI](https://fastapi.tiangolo.com/) bootstrapped with [`create-llama`](https://github.com/run-llama/LlamaIndexTS/tree/main/packages/create-llama).

The purpose of this AI chat app is to help users find suitable sports and groups to join. The main app is an AI RAG chat app. The app secondarily also serves a simple sports suggestor form.
By default the AI chat app is found at root URL and sports form is found at `/lajikysely.html`.

## Getting Started

First, setup the environment with poetry:

> **_Note:_** This step is not needed if you are using the dev-container.

```
poetry install
poetry shell
```

Then take a look at `.env.example` files for backend and frontend and create `.env` files based on them. (E.g. you might need to configure an `OPENAI_API_KEY` if you're using OpenAI as model provider).

If you are using any tools or data sources, you can update their config files in the `config` folder.

Add folder `storage` if it does not exist in root and add following files with content `{}`

- docstore.json
- graph_store.json
- image\_\_vector_store.json
- index_store.json

Second, generate the embeddings of the documents in the `./data` directory:

```
poetry run generate
```

Third, run the app:

```
poetry run dev
```

Open [http://localhost:8000](http://localhost:8000) with your browser to start the app.

The example provides two different API endpoints:

1. `/api/chat` - a streaming chat endpoint
2. `/api/chat/request` - a non-streaming chat endpoint

You can test the streaming endpoint with the following curl request:

```
curl --location 'localhost:8000/api/chat' \
--header 'Content-Type: application/json' \
--data '{ "messages": [{ "role": "user", "content": "Hello" }] }'
```

And for the non-streaming endpoint run:

```
curl --location 'localhost:8000/api/chat/request' \
--header 'Content-Type: application/json' \
--data '{ "messages": [{ "role": "user", "content": "Hello" }] }'
```

You can start editing the API endpoints by modifying `app/api/routers/chat.py`. The endpoints auto-update as you save the file. You can delete the endpoint you're not using.

To start the app optimized for **production**, run:

```
poetry run prod
```

## Deployments

For production deployments, check the [DEPLOY.md](DEPLOY.md) file.

## How to run with docker compose

First check setup instructions for both frontend and backend and set env's. Make sure you have docker installed. Create file `Caddyfile` in project root based on `Caddyfile.example`.

Then first run:

```
docker compose up -d
```

optionally before running `up` command, you can build images first individually or all at once:

```
docker compose build
```

or

```
docker compose build <service>
```

When services are up, generate AI embeddings (make sure you have correctly setup files in storage/storage_vol):

```
docker compose exec backend /bin/bash
poetry run generate
exit
```

## Learn More

To learn more about LlamaIndex, take a look at the following resources:

- [LlamaIndex Documentation](https://docs.llamaindex.ai) - learn about LlamaIndex.

You can check out [the LlamaIndex GitHub repository](https://github.com/run-llama/llama_index) - your feedback and contributions are welcome!

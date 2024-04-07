# Self-hosted Faster Whisper API, Compatible with OpenAI's Whisper API

## Apple Shortcut


### English 

<https://s.catstudio.app/buy/88508b33-0d52-4ad2-a4f5-0768afa17d9c>

### Traditional Chinese

Original version (OpenAI): <https://onenewbite.gumroad.com/l/whisper?layout=profile&recommended_by=library>


## Get Started (Docker Compose)

You'll need

1. A PC with NVIDIA GPU
2. Connected to the public internet to expose this service to the public

```shell
git clone https://github.com/imWildCat/faster-whisper-api.git
cd faster-whisper-api
cp .env.example .env
# Edit .env file to set your API key and Cloudflare Tunnel token (optional)

docker-compose up -d
```

### Use pre-built image

Open `docker-compose.yml`, apply this change

```diff
services:
  app:
-    build:
-      context: .
-      dockerfile: Dockerfile
+   image: ghcr.io/imwildcat/faster-whisper-api:main
````

Then run `docker-compose up -d` to start the service.
It would save you ~5 mins of building the image.


## License

The MIT License (MIT)

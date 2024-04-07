# Self-hosted Faster Whisper API, Compatible with OpenAI's Whisper API

## Apple Shortcut


### English 

* Self-hosted version: <https://www.icloud.com/shortcuts/fc52254d27cd4a10aba792f66510b3a6>
* OpenAI version: <https://www.icloud.com/shortcuts/59fc74df20fc4e54abba8afb91a5d562>

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

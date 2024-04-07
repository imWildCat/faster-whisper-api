# Self-hosted Faster Whisper API, Compatible with OpenAI's Whisper API

## 🍎 Apple Shortcut


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


# 自架 Faster Whisper API，兼容 OpenAI 的 Whisper API

## 🍎 Apple 快捷方式

### 英文

<https://s.catstudio.app/buy/88508b33-0d52-4ad2-a4f5-0768afa17d9c>

### 繁體中文

原始版本（OpenAI）: <https://onenewbite.gumroad.com/l/whisper?layout=profile&recommended_by=library>

## 開始（Docker Compose）

你需要：

1. 一臺帶有 NVIDIA GPU 的電腦
2. 連接到公共互聯網以將此服務暴露給公眾

```shell
git clone https://github.com/imWildCat/faster-whisper-api.git
cd faster-whisper-api
cp .env.example .env
# 編輯 .env 文件以設置您的 API 密鑰和 Cloudflare 隧道令牌（可選）

docker-compose up -d
```

### 使用預構建的鏡像

打開 `docker-compose.yml`，應用以下更改

```diff
services:
 app:
-  build:
-   context: .
-   dockerfile: Dockerfile
+  image: ghcr.io/imwildcat/faster-whisper-api:main
````

然後運行 `docker-compose up -d` 啟動服務。
這將節省您約 5 分鐘的鏡像構建時間。

## 許可證

MIT 許可證 (MIT)

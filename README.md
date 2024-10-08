# Appwrite Python SDK (Asynchronous Version)

![License](https://img.shields.io/github/license/appwrite/sdk-for-python.svg?style=flat-square)
![Version](https://img.shields.io/badge/api%20version-1.6.0-blue.svg?style=flat-square)
[![Build Status](https://img.shields.io/travis/com/appwrite/sdk-generator?style=flat-square)](https://travis-ci.com/appwrite/sdk-generator)
[![Twitter Account](https://img.shields.io/twitter/follow/appwrite?color=00acee&label=twitter&style=flat-square)](https://twitter.com/appwrite)
[![Discord](https://img.shields.io/discord/564160730845151244?label=discord&style=flat-square)](https://appwrite.io/discord)

**This SDK is compatible with Appwrite server version 1.6.x. For older versions, please check [previous releases](https://github.com/humarr/async-appwrite/releases).**

Appwrite is an open-source backend as a service server that abstract and simplify complex and repetitive development tasks behind a very simple to use REST API. Appwrite aims to help you develop your apps faster and in a more secure way. Use the Python SDK to integrate your app with the Appwrite server to easily start interacting with all of Appwrite backend APIs and tools asynchronously.

![Appwrite](https://github.com/appwrite/appwrite/raw/main/public/images/github.png)

## Installation

To install via [PyPI](https://pypi.org/):

```bash
pip install async_appwrite
```


## Getting Started

### Init your SDK
Initialize your SDK with your Appwrite server API endpoint and project ID which can be found on your project settings page and your new API secret Key from project's API keys section.

```python
from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_users import AsyncUsers

client = AsyncClient()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)
```

### Make Your First Request
Once your SDK object is set, create any of the Appwrite service objects and choose any request to send. Full documentation for any service method you would like to use can be found in your SDK documentation.

```python

users = AsyncUsers(client)

async def create_user():
    result = await users.create(ID.unique(), email="email@example.com", phone="+123456789", password="password", name="Walter O'Brien")
    return result

if __name__ == "__main__":
    user_result = asyncio.run(create_user())
    print(user_result)
```

### Full Example
```python
from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_users import AsyncUsers
from appwrite.id import ID
import asyncio

client = AsyncClient()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

users = AsyncUsers(client)

async def create_user():
    result = await users.create(ID.unique(), email="email@example.com", phone="+123456789", password="password", name="Walter O'Brien")
    return result

if __name__ == "__main__":
    user_result = asyncio.run(create_user())
    print(user_result)

```

### Error Handling
The Appwrite Python SDK raises `AppwriteException` object with `message`, `code` and `response` properties. You can handle any errors by catching `AppwriteException` and present the `message` to the user or handle it yourself based on the provided error information. Below is an example.

```python
users = AsyncUsers(client)
async def create_user():
    try:
        result = await users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")
    except AppwriteException as e:
        print(e.message)

if __name__ == "__main__":
    user_result = asyncio.run(create_user())
    print(user_result)
```

### Learn more
You can use the following resources to learn more and get help
- 🚂 [Async Appwrite Python Playground](https://github.com/Humarr/async_appwrite_playground-for-python)



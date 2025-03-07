# BoxAPI Python

A Python client for interacting with the [Box API](https://boxapi.ir) for Instagram. This library wraps multiple Instagram endpoints including user information, media retrieval, and direct messages, allowing you to easily integrate Instagram functionality into your Python applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [General Instagram API](#general-instagram-api)
  - [Direct Messages](#direct-messages)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Modular Design**: Separate sub-clients for general Instagram endpoints and direct message (DM) endpoints.
- **Easy Integration**: Instantiate a single client to access the full functionality of the Box API.
- **Flexible Usage**: Use DM endpoints only when needed—save overhead if your application doesn’t require them.
- **Extensible**: Add additional endpoints or support for other platforms with minimal changes.

## Installation

You can install the package via [pip](https://pypi.org/project/pip/) or [Poetry](https://python-poetry.org/).

### Using pip

```bash
pip install boxapi
```

### Using Poetry

```bash
poetry add boxapi
```

## Project Structure

```
boxapi-python/
├── boxapi/
│   ├── __init__.py              # Package initializer, re-exports public API
│   ├── constants.py             # Global constants and endpoint paths
│   ├── client.py                # BoxApiClient: top-level client for Box API
│   ├── instagram/
│   │   ├── __init__.py          # Makes the instagram module importable
│   │   ├── api_client.py        # InstagramAPIClient: general Instagram endpoints
│   │   └── dm_client.py         # InstagramDMClient: direct message endpoints
│   └── utils/
│       └── base_url_session.py  # Custom session with base URL support
├── examples/                    # Example scripts demonstrating usage
├── tests/                       # (Optional) Unit tests
├── pyproject.toml               # Build configuration for Poetry
├── LICENSE                      # License file
└── README.md                    # This file
```

## Usage

### General Instagram API

```python
from boxapi import BoxApiClient

# Initialize BoxApiClient with Box API credentials
# IMPORTANT: MAKE SURE YOU ARE READING YOUR USERNAME AND PASSWORD FROM ENVIRONMENT VARIABLES
box_client = BoxApiClient("your_boxapi_username", "your_boxapi_password")

# Use the Instagram sub-client for general endpoints
user_info = box_client.instagram.get_user_info("leomessi")

print(user_info)
```

### Direct Messages

Direct Message functionality is available through a separate sub-client. Instantiate it when needed:

```python
from boxapi import BoxApiClient

# Initialize BoxApiClient with Box API credentials
box_client = BoxApiClient("your_boxapi_username", "your_boxapi_password")

# Use DM endpoints by providing the Instagram account credentials per call
login_response = box_client.instagram_dm.direct_login("insta_username", "insta_password")
print(login_response)
```

## Examples

Check out the [examples](./examples) folder for complete scripts demonstrating how to use the different features of this library (It's a work in progress).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please review our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

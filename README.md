# Legit Ink Tattoo API

A FastAPI-based backend service for the Legit Ink Tattoo booking system.

## Description

This API provides backend functionality for the Legit Ink Tattoo application, including integration with Instagram feeds for displaying tattoo portfolio and updates.

## Features

- Instagram feed integration to fetch and display media posts
- CORS support for frontend integration
- FastAPI framework for high performance and automatic API documentation

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Tattoo_booking_BE
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Instagram access token:
   ```
   INSTAGRAM_TOKEN=your_instagram_access_token_here
   ```

## Usage

Run the application using uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

The API will be available at `http://localhost:5000`

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

## API Endpoints

### Root
- **GET** `/`
  - Returns a welcome message
  - Response: `{"message": "Legit Ink Tattoo API"}`

### Instagram Feed
- **GET** `/api/v1/instafeed/`
  - Fetches Instagram media posts
  - Requires `INSTAGRAM_TOKEN` environment variable
  - Response: JSON array of Instagram media objects with fields: id, caption, media_url, permalink, media_type

## Environment Variables

- `INSTAGRAM_TOKEN`: Instagram Graph API access token for fetching feed data

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **httpx**: Asynchronous HTTP client
- **python-dotenv**: Environment variable management
- **uvicorn**: ASGI server for running FastAPI applications

## CORS Configuration

The API is configured to allow requests from:
- `https://legit-ink-tatoo.vercel.app/`
- `http://localhost:5000`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license information here]

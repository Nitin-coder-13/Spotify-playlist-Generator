# Spotify Playlist Generator

A Python-based application that demonstrates Spotify API integration using the Spotipy library. This project allows users to generate and manage Spotify playlists programmatically.

## Features

- 🎵 Generate custom Spotify playlists
- 🔌 Spotify API integration using Spotipy
- 🐍 Clean Python implementation
- 📊 Demonstrates RESTful API calling patterns

## Technologies Used

- **Python** - Core programming language
- **Spotipy** - Spotify Web API wrapper for Python
- **Spotify API** - Music data and playlist management

## Prerequisites

Before running this project, ensure you have:

- Python 3.7 or higher installed
- A Spotify account
- Spotify API credentials (Client ID and Client Secret)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spotify-playlist-generator.git
cd spotify-playlist-generator
```

2. Install required dependencies:
```bash
pip install spotipy
```

3. Set up your Spotify API credentials:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new app
   - Copy your Client ID and Client Secret
   - Set up your redirect URI

4. Create a `.env` file or configure your credentials:
```
SPOTIPY_CLIENT_ID='your-client-id'
SPOTIPY_CLIENT_SECRET='your-client-secret'
SPOTIPY_REDIRECT_URI='your-redirect-uri'
```

## Usage

Run the application:
```bash
python main.py
```

Follow the prompts to authenticate with Spotify and generate your playlist.

## Project Structure

```
spotify-playlist-generator/
├── main.py              # Main application file
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not tracked)
└── README.md           # Project documentation
```

## API Documentation

This project uses the [Spotify Web API](https://developer.spotify.com/documentation/web-api/) through the Spotipy library. Key endpoints used include:

- User authentication
- Playlist creation
- Track search and addition

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

## Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ If you found this project helpful, please consider giving it a star!

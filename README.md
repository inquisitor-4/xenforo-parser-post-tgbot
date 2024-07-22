
# Telegram Bot Finder for XenForo Forum Posts

Welcome to the Telegram Bot Finder for XenForo Forum Posts! This bot enables you to search for posts or subforums on a specified XenForo forum directly from Telegram. Leveraging Docker and Python, this bot ensures a seamless and efficient experience.

## Features

- **Search XenForo Forum Posts:** Simply send a keyword to the bot and receive relevant forum posts or subforums containing the keyword.
- **Easy Deployment:** Quickly deploy the bot using Docker for a hassle-free setup.
- **Robust Web Scraping:** Utilizes BeautifulSoup and requests for reliable web scraping.
- **Efficient:** Designed to handle searches quickly and accurately.

## Prerequisites

- Docker
- Docker Compose
- A Telegram bot token from [BotFather](https://t.me/BotFather)

## Installation

1. **Clone the Repository:**

    ```sh
    git clone git@github.com:inquisitor-4/xenforo-parser-post-tgbot.git
    cd xenforo-parser-post-tgbot
    ```

2. **Set up your environment variables:**

    Create a `.env` file in the root directory of the project and add your Telegram bot token:

    ```env
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    FORUM_URL=http://forum.ander-services.asia
    ```

3. **Build and run the Docker containers:**

    ```sh
    docker-compose up -d
    ```

## Project Structure

/xenforo-parser-post-tgbot 
|-- src
 | |-- bot.py 
|-- .env 
|-- Dockerfile 
|-- requirements.txt 
|-- docker-compose.yml 
|-- README.md


## Usage

1. **Start the Bot:**

    Ensure your Docker containers are running:

    ```sh
    docker-compose up -d
    ```

2. **Interact with the Bot:**

    Open Telegram and start a chat with your bot. Use the `/start` command to begin, and send keywords to search the forum.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

License This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or [contact with me](https://github.com/inquisitor-4/inquisitor-4?tab=readme-ov-file#connect-with-me).

---

Thank you for using the Telegram Bot Finder for XenForo Forum Posts! We hope it provides a valuable and efficient tool for your forum searches.

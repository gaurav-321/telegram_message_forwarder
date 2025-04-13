# 📌 Telegram Message Forwarder

Telegram Message Forwarder is a Python script designed to automate the forwarding of messages from specified Telegram channels to a designated group chat. It simplifies the process of keeping important updates organized and accessible.

## ✨ Description

This project provides a robust solution for channel administrators who want to ensure that critical information is disseminated efficiently within their organization. By using Telethon, a Python library for interacting with Telegram's API, this script can handle real-time message forwarding, making it an invaluable tool for maintaining communication channels.

## 🚀 Features
- **Automated Message Forwarding**: Messages from specified channels are automatically forwarded to a designated group chat.
- **Real-Time Updates**: Ensures that critical information is disseminated instantly without manual intervention.
- **Easy Setup**: Simple installation and configuration process, making it accessible even for beginners.

## ⛓ Installation

To get started with Telegram Message Forwarder, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/telegram_message_forwarder.git
   cd telegram_message_forwarder
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 📦 Usage

Here’s how you can use the Telegram Message Forwarder:

```python
# Import the main function from the script
from telegram_forwarder import run_forwarder

# Run the message forwarding process
run_forwarder()
```

### Example Configuration

To configure the script, create a `.env` file in the project root with the following content:

```env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
CHANNELS=@channel1 @channel2
FORWARD_GROUP=@forward_group
```

Replace `your_api_id`, `your_api_hash`, and channel/group handles with your actual values.

## 🔧 Configuration

The script relies on environment variables to configure the Telegram API connection, channels, and forwarding group. Ensure that you have a `.env` file set up as described above.

## 🧪 Tests

This project includes basic tests to ensure that the message forwarding functionality works as expected. You can run these tests using:

```sh
pytest
```

Make sure you have `pytest` installed:
```sh
pip install pytest
```

## 📁 Project Structure

The project structure is straightforward:

```
telegram_message_forwarder/
├── README.md
├── requirements.txt
└── telegram_forwarder.py
```

- **README.md**: This file.
- **requirements.txt**: Lists the project dependencies.
- **telegram_forwarder.py**: The main script for message forwarding.

## 🙌 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance! 🚀
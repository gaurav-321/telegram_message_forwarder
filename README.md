# Telegram Message Forwarder

This Python script forwards messages from specified channels to a designated group chat using the Telegram API.

## Prerequisites

- **API Credentials**: Obtain your API credentials from [Telegram's website](https://my.telegram.org/auth).
- **Phone Number**: Provide your phone number including the country code.
- **Forward Group**: Specify the group ID where you want to forward messages.
- **Channels**: Provide a comma-separated list of channel IDs from which you want to forward messages.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/gaurav-321/telegram_message_forwarder.git
   cd telegram_message_forwarder

2. Install the required Python packages:
    ```python
    pip install -r requirements.txt
3. Create a .env file in the root directory and add your API credentials, phone number, forward group, and channels as follows:
    ```
    api_id=your_api_id
    api_hash=your_api_hash
    phone_number=your_phone_number
    forward_group=forward_group_id
    channels=channel_id1,channel_id2,channel_id3


## Usage
Run the script using Python:
   ```python
   python telegram_forwarder.py
   ```
## License
This project is licensed under the MIT License - see the LICENSE file for details.
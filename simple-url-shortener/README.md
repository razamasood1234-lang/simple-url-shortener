# Simple URL Shortener

A lightweight, command-line URL shortener built in Python. Similar to services like Bitly but designed for learning purposes, this tool converts long URLs into manageable short codes using a hash-based algorithm.

## Features

- **Shorten Long URLs:** Convert any long URL into a unique 6-character code.
- **Retrieve Original URLs:** Easily get back the original URL using its short code.
- **In-Memory Storage:** Uses a Python dictionary for fast lookups (data persists only during runtime).
- **Collision Handling:** Intelligently resolves hash collisions to guarantee unique short codes.
- **User-Friendly CLI:** Simple text-based interface with clear commands and feedback.
- **List All URLs:** View all shortened URLs and their mappings in a clean, formatted list.

## Technology Stack

- **Language:** Python 3
- **Libraries:** `hashlib`, `random`, `string` (All are part of the Python Standard Library)

## Installation

1.  **Clone or Download the Project:**
    ```bash
    git clone <your-repository-url>
    cd simple-url-shortener
    ```
    *(Alternatively, just download the `url_shortener.py` file.)*

2.  **Ensure Python 3 is installed** on your system. You can check by running:
    ```bash
    python --version
    # or
    python3 --version
    ```

## Usage

1.  Navigate to the project directory in your terminal.
2.  Run the application:
    ```bash
    python url_shortener.py
    ```
3.  You will be greeted with a menu of commands. Use the following options:

    | Command | Description | Example |
    | :--- | :--- | :--- |
    | `shorten <URL>` | Shortens a given URL. | `shorten https://www.example.com/very-long-path` |
    | `lookup <CODE>` | Retrieves the original URL for a short code. | `lookup a3f8d2` |
    | `list` | Displays all shortened URLs and their codes. | `list` |
    | `help` | Shows the help menu with all commands. | `help` |
    | `exit` | Exits the program gracefully. | `exit` |

### Example Session

```bash
$ python url_shortener.py
==================================================
        SIMPLE URL SHORTENER
==================================================
Commands:
  shorten <URL>    - Shorten a URL
  lookup <code>    - Retrieve original URL
  list             - Show all shortened URLs
  exit             - Quit the program
==================================================

Enter command: shorten https://www.github.com/search?q=python+projects
✅ Shortened successfully!
   Original: https://www.github.com/search?q=python+projects
   Short: http://short.url/d9e1b4

Enter command: lookup d9e1b4
✅ Original URL found:
   http://short.url/d9e1b4 -> https://www.github.com/search?q=python+projects

Enter command: list
📋 All Shortened URLs (1 total):
------------------------------------------------------------
d9e1b4 -> https://www.github.com/search?q=python+projects
------------------------------------------------------------

Enter command: exit
Thank you for using the URL Shortener. Goodbye!
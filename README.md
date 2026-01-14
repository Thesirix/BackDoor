# 🔓 BackDoor

This project is a simple implementation of a backdoor in Python, allowing a remote user to execute commands on a target computer remotely.

## ✨ Features

- **🔌 Client-server connection:** The project uses sockets to establish a connection between a client and a server, enabling bidirectional communication.
- **💻 System command execution:** The server can receive commands from the client and execute them on the target computer. This allows the remote user to control the computer remotely.
- **🛠️ Additional features:**
  - The server can retrieve system information such as the platform and current directory.
  - The server can change the working directory on the target computer.
  - The server can download files from the target computer.
  - The server can capture screenshots of the target computer 📸.

## 📂 Project Structure

The project consists of two Python files:

- `serveur.py`: The server code that runs on the target computer. It waits for incoming connections from clients and executes received commands.
- `client.py`: The client code that runs on the remote user's computer. It connects to the server and sends commands to be executed.

## 🚀 Usage

1. **Run the server:**

   - Run the `serveur.py` file on the target computer using Python.
   - Ensure the port specified in the file is accessible from the outside if you plan to access it remotely.

2. **Run the client:**

   - Run the `client.py` file on the remote user's computer using Python.
   - Specify the IP address and port of the server you wish to connect to.

3. **Send commands:**

   - Once connected, you can send commands to the server from the client using the appropriate syntax.
   - For example, you can type `ls` to list files in the current directory, `cd <directory>` to change directory, `dl <file>` to download a file, or `capture <name>` to capture a screenshot.

4. **Close the connection:**
   - To exit the session, you can close the client and server by pressing `Ctrl+C` or by closing the console windows.

## ⚠️ Security

It is important to note that this project is for **educational and research purposes only**. Using this backdoor without appropriate consent may violate privacy and computer security laws. Please ensure you use this project only legally and ethically, and with the explicit consent of the parties involved.

## ❤️ Contributions

Contributions in the form of suggestions, bug reports, or feature requests are welcome. Feel free to open an issue or submit a pull request on GitHub.

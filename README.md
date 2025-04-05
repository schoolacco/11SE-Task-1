# NASA Program

This Python program allows you to retrieve NASA information from an external API. The program uses the `requests` library to fetch data from NASA's API as well as `tkinter` and `tkinterweb` as well as `pywebview` to insert the entire program into a GUI and `webbrowser` to open up your default browser.

## Features

- Fetch the current and previous APOD's data and display it in the GUI.
- Open the APOD's image URL in your default browser.
- Fetch images from NASA's earth images service based on latitude and longtitude (very limited).
- Open the Earth images' image URL in your default browser.

## Requirements

To run this program, you need to install the following dependencies:

- `tkinterweb` to allow for html within the tkinter GUIs
- `requests` to make HTTP requests to the NASA API.
- `pywebview` to view the earth images within a GUI

### Install dependencies

To install the required dependencies, you can run:

```bash
pip install -r requirements.txt

```

Or if it fails:

```bash
pip install tkinterweb
pip install requests
pip install pywebview

```

# Keyboard Language Flag Tracker

This Python tool tracks the mouse pointer and displays the flag of the current keyboard language along the mouse cursor.

You can also build an .exe file and add it to system startup to have a keyboard layout hint at hand all the time.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd displanger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. The flag of the current keyboard language will be displayed alongside the mouse pointer.

## Building the distributive

Run /utils/build.cmd to ensure proper .exe file creation.

After the .exe file has been built, you can start or stop the application using the appropriate scripts in the ```/utils``` folder.

## Adding to startup

1. Create a shortcut for /utils/start.cmd

2. Press ```Start+R``` on keyboard, type ```shell:startup``` and press Enter.

3. Move the shortcut to the folder that just has opened

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the GNU GPL 3 License.

## Credits

Initial flag images are from https://openclipart.org/ .
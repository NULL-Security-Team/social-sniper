<h1 align="center"> Social Sniper</h1>
This is a Python script that searches for a given username on various social media platforms. It takes in a username as an argument and can optionally run in threaded mode, verbose mode, or save the results to a file.

<p align="center">
    <img width="400" src="https://user-images.githubusercontent.com/48811414/86419313-9c4e1500-bcca-11ea-9fe2-5137577aed61.PNG" alt="Null Security Team">
</p>


## Installation
- `git clone https://github.com/sircryptic/social-sniper`
- `cd social-sniper`
- `pip install -r requirements.txt`

## Example Usage

To use this script, run the following command in a terminal:
```
python3 ssniper.py exampleuser -v -t -s
```

Here's what each of the flags do:

- `-t` or `--threaded`: Run the script in threaded mode, which can speed up the scanning process. Note that this mode may cause some results to be printed out of order.
- `-v` or `--verbose`: Print out additional information about each search, ie when the username is not found on a platform.
- `-s` or `--save`: Saves the results to a file with the same name as the username.

## Configuration

The list of social media platforms to search can be configured in the `socials.txt` file. Each line in this file should contain a platform name and a URL with the string `<user>` where the username should be inserted.

## Credits
- ⭐ sircryptic @ NullSecurityTeam ~ fetching back dead tool
- ⭐ 0XJACK @ DeleteHumanity ~ base design

Very basic OpenAI client for the command line.
This is my personal CLI script. Use it if you feel like it but be sure to configure it to your needs.
This README is mostly a reminder to myself, to remember how to set it up.

## Setup
- Clone the repository (e.g.: `/.../howto-cli`)
- Link script so it can be used as `howto`: `ln -s /.../howto-cli/main.py ~/.local/bin/howto`
- Add alias so `hi` starts interactive mode: `alias hi="howto -i"`


## Usage
Basic usage expects you to pass your question as command line arguments. Examples:
```
❯ howto scan for IPs on my LAN  
» On Arch Linux, what is the command line command to scan for IPs on my LAN?
« sudo nmap -sn {IP range}
```

```
❯ howto resize png to 600x400 
» On Arch Linux, what is the command line command to resize png to 600x400?
« convert input.png -resize 600x400 output.png
```

Additionally, you can start interactive mode to ask follow-up questions, similar to how a conversation might work when using ChatGPT.
Run `howto -i` or `hi` if you're using the alias above.


## Configuration
You need an [OpenAI API key](https://platform.openai.com/account/api-keys) to use their API and this script.
Once you have generated an API key, use `howto -c` to configure the key for this script.


## Acknowledgements
Inspired by [gynvael's howto script](https://gynvael.coldwind.pl/?id=771)

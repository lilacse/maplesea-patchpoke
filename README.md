# maplesea-patchpoke

Simple Python script to periodically check if the MapleSEA manual patch you need is available on PlayPark servers. Useful during patch day. Especially useful if you want to download the latest patch as soon as possible but you are busy and need to do something else instead of refreshing the link in your browser every minute (and have no friends available to do the work for you as well). 

Personally, when it's a patch day, I run this script in the background approximately 2 hours before the servers are expected to go live. A notification will be raised if the link this script is looking at points to a patch file. It does not *immediately* notifies you upon file upload (it is impossible by technology), but should notify you soon enough before server goes live and the download page gets updated. 

***Note:** Does not work for small MapleStory.exe updates. Not like it matters a lot, they take almost no time to install anyway.*

### Dependencies

- Python 3.x
- [Requests](https://requests.readthedocs.io/en/master/)
- [Plyer](https://github.com/kivy/plyer)

Assume that this script works with the latest versions of the dependencies listed above - submit an issue if any updates on dependencies broke it. You can install Requests and Plyer after installing Python by using their respective `pip install` commands (refer to their pages for it). 

### Usage

First, clone/download this repo to some place you can execute files. Then, in a command line (Command Prompt or Powershell, you choose), `cd` to the directory where this repo is, then run 

```
python main.py
```

Yeah, that's quite it and the rest should be self-explanatory. You should configure the script before actually running it, but that is for the next section. 

No GUI is provided but- why do you need a GUI for something that you won't really need to look at anyway?

***Note**: If you associated Python files properly during Python's installation, you can likely run it by just double-clicking on `main.py`. You still need to configure it using the section below, though.*

### Configuration

No, this script does not use a config file (although I should make it use a config file some day). To configure, directly open the script in a text editor (Notepad is good, but you can use whatever more fancy) and head for the `# parameters` section. Edit the values there to fit your requirements. 

| Variable | Description | 
| - | - |
| `from_patch` | Your current MapleSEA client version. Minor updates to MapleStory.exe does not count. For example, v199.3 is just `199` for this field.|
| `to_patch` | The version you are trying to download. If you are not doing anything special, it should be `from_patch + 1`. So if `from_patch` is `199`, `to_patch` should be `200`.|
| `url` | **You should not edit this.** If you believe the URL stopped working, submit an issue. 
| `min_wait` | Minimum amount of time in seconds the script waits before poking the link again. Default values should be fine, please do not set it to too low and turn your patch poking into a denial-of-service attempt. |
| `max_wait` | Maximum amount of time in seconds the script waits before poking the link again. Must be at least equal or larger than `min_wait`. Default values should also be fine. 
| `use_notification` | If set to `True` (the default), a Windows notification will be triggered if the link points to a patch file. No real reasons to turn this to `False` unless you don't want notifications (and I don't know why you want to run this if you don't want notifications). 

### Disclaimer

This is a completely personal project born out of my free time - it is unrelated to anyone or anything else. Use it carefully and wisely. I hold zero responsibilities for anything that happens related to the use of this. 

### License

[Unlicense](https://unlicense.org). Do whatever you want with the code. See [LICENSE](https://github.com/lilacse/maplesea-patchpoke/blob/main/LICENSE) for the full terms. 

Do note that any contributions (if any) will also go under the same license. Check unlicense.org for more information on this. 
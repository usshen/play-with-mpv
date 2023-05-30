# Play with MPV
Chrome extension and python server that allows you to play videos in webpages with MPV instead.  
Works on [hundreds of sites](https://rg3.github.io/youtube-dl/supportedsites.html) thanks to youtube-dl,
and even torrents if you install [peerflix](https://github.com/mafintosh/peerflix).

## Installation(Windows)
1. Install [MPV](https://mpv.io/installation/)(recommended) Install through [chocolaty](https://chocolatey.org/install#individual)
2. Install [chrome extension](https://chrome.google.com/webstore/detail/play-with-mpv/hahklcmnfgffdlchjigehabfbiigleji)
3. Install yt-dlp through your package manager for frequent updates.  
4. Download the release 
5. Start server by running `play with mpv.exe`


## Usage
Right-click [this link](https://www.youtube.com/watch?v=dQw4w9WgXcQ) and select "Play with MPV".
MPV should popup and start playing the video. (Ctrl+Space also works)

![screenshot](https://github.com/thann/play-with-mpv/raw/master/screenshot.png)

## Autostart
- Linux: `cp {/usr,~/.local}/share/applications/thann.play-with-mpv.desktop ~/.config/autostart`
- MacOS: [instructions](https://stackoverflow.com/questions/29338066/mac-osx-execute-a-python-script-at-startup)
- Windows [instructions](https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts)

## Protips
MPV is [highly configurable](https://mpv.io/manual/stable/), this is just how I like to use it.

To start in the corner, have no border, and stay on top: edit `~/.config/mpv/mpv.conf`
```
ontop=yes
border=no
window-scale=0.4
geometry=100%:100%
```

In order to resize the window without borders, add keybinds: edit `~/.config/mpv/input.conf`
```
` cycle border
ALT+UP add window-scale 0.05
ALT+DOWN add window-scale -0.05
```

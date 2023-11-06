## /usr/bin/vim-remote

```bash
##!/usr/bin/env bash

EXTRAER_DE_URL='\/var\/www\/'

function urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }

arg=$(urldecode "${1}")

# Get the file path.
file=$(echo "${arg}" | cut -d= -f2 | cut -d\& -f1)

file=$(echo $file | sed "s/$EXTRAER_DE_URL//")

# Get the line number.
line=$(echo "${arg}" | cut -d= -f3)

if [ -z $line ] ; then
	vim --servername SERVER --remote-tab "$file"
else
	vim --servername SERVER --remote-tab "$file" +$line
fi
```

## .local/share/applications/vim.desktop

```
[Desktop Entry]
Name=Vim Text Editor
Comment=Edit text files
Exec=/usr/bin/vim-remote %f %line
Terminal=true
Type=Application
Icon=terminal
Categories=Utility;TextEditor;
StartupNotify=true
MimeType=text/plain;text/x-makefile;text/x-c++hdr;text/x-c++src;text/x-chdr;text/x-csrc;text/x-java;text/x-moc;text/x-pascal;text/x-tcl;text/x-tex;application/x-shellscript;text/x-c;text/x-c++;text/php;x-scheme-handler/phpstorm;x-scheme-handler/pstorm;x-scheme-handler/txmt;
```

## .local/share/applications/mimeapps.list

```
[Default Applications]
x-scheme-handler/tg=telegramdesktop.desktop
text/plain=vim.desktop
text/markdown=vim.desktop
text/html=vim.desktop
x-scheme-handler/phpstorm=vim.desktop
```

# Roamer [![Build Status](https://travis-ci.org/abaldwin88/roamer.svg?branch=master)](https://travis-ci.org/abaldwin88/roamer)
### The Plain Text File Manager

[gif here]

Roamer turns your favorite text editor into a lightweight file manager.  Copy, Cut & Paste files en masse without leaving your terminal window.

## Install
#### Requirements
* Python version: 2.7+, 3.2+
* OS: Linux, MacOS, Windows WSL (Windows Subsystem for Linux)

#### Command
```shell
sudo pip install roamer
```

For a high security install see [here](doc/faq.md).

## Usage

### Start Roamer
```shell
$ roamer
```
This will open the current working directory in your default $EDITOR.  (See options section to override editor)

### Example Output
```shell
" pwd: /Users/abaldwin/Desktop/stuff
my_directory/ | b0556598b8f8
my_file_1.txt | ce9b0a287985
my_file_2.txt | fc3da7f790a6
my_file_3.txt | fc3da7f790a6
```

### Explanation

* Each line represents a single entry (file or directory)
* On the left side of the pipe character is the entry's name
* On the right side is the entry's hash.  You can think of the hash as a link to that entry's contents.
* A line starting with double quote (") is a comment and will be ignored.

--> Make changes as desired.  When finished save and quit to commit the changes.  e.g.  vim `:wq`

### Common Operations

#### Delete a file
 * Delete the line

#### Copy a file
* Copy the entire line
* Paste it onto a new line

#### Rename a file
* Type over the existing file's name
* Do not modify the hash on the right side

#### Make a new empty file
* Add a new line
* Type the new file's name

#### Move files between directories
* Open up another terminal tab and run second roamer session
* Copy / Paste lines between both sessions of roamer



## Options

#### Editor
Roamer uses your default $EDITOR environment variable.

To override a specific editor for roamer add this to your shell's config. (~/.bashrc   ~/.zshrc  etc)
```shell
export ROAMER_EDITOR=emacs
```

If no editor is set then vi will be used.

#### Data Directory
Roamer needs a directory for storing data between sessions.  By default this will be saved in `.roamer-data` in your home directory.

To override:
```shell
export ROAMER_DATA_PATH=~/meh/
```


## Editor Plugins

This roamer library is editor agnostic and focused on processing plain text.  To enhance your experience with roamer consider installing roamer editor plug-ins for syntax highlighting, shortcuts, etc.

* https://github.com/abaldwin88/roamer.vim

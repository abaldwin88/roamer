# FAQs

#### High Security Install?

Steps for installing roamer without using sudo...

```shell
pip install --user roamer
```

Check that `~/.local/bin` is in your PATH
```shell
echo "$PATH"|grep -q ~/.local/bin && echo "Ready to use roamer!"
```

Add `~/.local/bin` to your PATH:
```shell
# Bash Users
echo "export PATH=\$PATH:~/.local/bin" >> ~/.bashrc
source ~/.bashrc

# Z Shell Users
echo "export PATH=\$PATH:~/.local/bin" >> ~/.zshrc
source ~/.zshrc
```

### Any Text Editor?

Roamer should work with any text editor that blocks.  That is any editor that lets you write messages with `git commit`.    ( e.g. Atom's `--wait` flag )

Tested Editors:

* vi
* nano
* vim
* emacs
* neovim
* atom
* sublime text 3
* vscode

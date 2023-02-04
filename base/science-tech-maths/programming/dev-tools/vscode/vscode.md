# Visual Studio Code

- [Keyboard shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

## Set working directory for debug

Add `"cwd": "${fileDirname}"` in `launch.json`

```json
{
    "version": "0.2.0",
    "configurations":
    {
            "name": "Python: Current File (Integrated Terminal)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${fileDirname}",
            "justMyCode": false
    }
}
```

## Unresolved import warnings

- <https://github.com/microsoft/python-language-server/blob/master/TROUBLESHOOTING.md#unresolved-import-warnings>

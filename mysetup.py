import subprocess, os, json
TARGET = "C:\\Users\\19njonebe\\AppData\\Roaming\\Code\\User\\settings.json" if os.path.isfile("C:\\Users\\19njonebe\\AppData\\Roaming\\Code\\User\\settings.json") else "C:\\Users\\19njonebe.STRS\\AppData\\Roaming\\Code\\User\\settings.json"
json.dump(json.loads("".join(open(TARGET).readlines()).replace(",\n}", "}")) | {"http.proxyStrictSSL": False, "git.enabled": True, "git.path": "C:\\Program Files\\GitHub Desktop\\resources\\app\\git\\cmd\\git.exe"}, open(TARGET, "w"))
(subprocess.call(["pip", "install", "cs50", "flask-session"]), [os.system("code --install-extension " + i) for i in ["PKief.material-icon-theme", "eamodio.gitlens", "github.github-vscode-theme"]])
json.dump(json.loads("".join(open(TARGET).readlines()).replace(",\n}", "}")) | {"workbench.colorTheme": "GitHub Dark", "workbench.iconTheme": "material-icon-theme"}, open(TARGET, "w"))
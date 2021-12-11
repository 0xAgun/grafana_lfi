<p align="center">
  <a href="https://github.com/0xAgun/grafana_lfi/">
    <img src="https://img.shields.io/badge/version-0.5.7-brightgreen?style=for-the-badge&logo=appveyor">
  </a>
  <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/badge/python-3x-orange?style=for-the-badge&logo=appveyor">
  </a>
  <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/badge/license-0xAgun-informational?style=for-the-badge&logo=appveyor">
  </a>
    <a href="https://github.com/0xAgun/grafana_lfi/">
      <img src="https://img.shields.io/github/forks/0xAgun/grafana_lfi?style=for-the-badge">
  </a>
</p>
<h1 align="center">
    Grafana LFI auto Exploit using Django
  <br>
</h1>
<h4 align="center">Grafana has a public API endpoint, /public/plugins/:pluginId, which allows you to view a plugin's assets. This works by providing a valid :pluginId and then specifying the file path, such as img/logo.png. However, Grafana fails to sanitize the user provided file path, leading to path traversal.</h4>
<hr>


## Requirements

Install these packge before using the script

```bash
  pip3 install django
  pip3 install urllib3==1.24.3
```
## Screenshots

![App Screenshot](https://i.imgur.com/eekh2NA.png)
![App Screenshot](https://i.imgur.com/il1HuIx.png)


## How to Use

To start the script, run the following command

```bash
  python3 manage.py runserver
```
after that go to http://127.0.0.1:8000/ to browse the interface,
and now just put you'r url without / in the last

## Disclaimer

This tool is for educational purpose only, please Don't use this tool for any kind of illigal or mallicious activites.
Any misuse of the tool is completelty at your risk.
I'm not responsile !!

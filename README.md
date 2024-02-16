# XBLScrapper
XBLScrapper is a Python tool for collecting a list of friends from an initial gamertag on Xbox Live (Xbox Network).

<img src="https://cdn.discordapp.com/attachments/1202826255523913781/1208111554956886036/Screenshot_1.png?ex=65e21890&is=65cfa390&hm=1936e9fe14a26cb80e28fd268a962e89bad6370d1839d38297868f0d6c50afc4&">

# Prerequisites
- [Python](https://www.python.org/downloads/)
- [OpenXBL - Api key](https://xbl.io/)

# How to Use
##### 1. Download the source:
Click on the green button ```CODE``` and then click on ```Dowload ZIP```

##### 2. Extract the files:
Extract the files and navigate to `resources/constants.json`. Insert your [API key](https://xbl.io/) into `constants.json`.
```json
{
    "XBL_API_KEY": "YOUR API KEY"
}
```

##### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

##### 4. Run the code:
```bash
py main.py
```

# Author
- Discord: @codaxy
- Telegram: @c0daxy

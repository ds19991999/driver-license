# 一个车牌号识别系统的小脚本

[![GitHub issues](https://img.shields.io/github/issues/ds19991999/driver-license.svg)](https://github.com/ds19991999/driver-license/issues)
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)](https://github.com/ds19991999/driver-license/blob/master/LICENSE)

## 运行环境

* `Python3 MySQL5.7 Debian`

## 依赖的包
```
sudo python3 -m pip install Pillow opencv-python
sudo apt-get install python3-tk
sudo apt-get install python3-pil.imagetk
```

## 代码结构
```
.
├── app.py
├── Card_Img
│   ├── cAA662F.jpg
│   ├── car3.jpg
│   ├── car4.jpg
│   ├── car5.jpg
│   ├── car7.jpg
│   ├── lLD9016.jpg
│   ├── wA87271.jpg
│   ├── wATH859.jpg
│   └── wAUB816.jpg
├── config.py
├── Core
│   ├── config.js
│   ├── find_license.py
│   ├── __init__.py
│   ├── predict.py
│   ├── Surface.py
│   ├── SVM
│   │   ├── svmchinese.dat
│   │   └── svm.dat
│   ├── Test
│   │   └── car.jpg
│   └── Train
│       ├── chars2.7z
│       └── charsChinese.7z
├── demo.gif
├── LICENSE
├── README.md
└── SQLHelper
    ├── __init__.py
    └── MySQLHelper.py
```

## 运行实例
```
git clone https://github.com/ds19991999/driver-license.git
cd driver-license
python3 app.py
```
![](./demo.gif)

## 参考
* https://blog.csdn.net/chenkz123/article/details/84949510

## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
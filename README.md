## 网络安全宣传周钓鱼体验工具

### 0x01 install

需要安装python3环境，然后安装依赖

```bash
python -m pip install -r requirements.txt
```

然后将play.py打包成exe

```
pyinstaller play.spec
```

然后将exe放入`其他资料/.__MACOS__/.__MACOS__/._MACOS_/`，并且替换掉test.avi视频为需要的内容，不要变更文件类型和文件名

### 0x02 enjoy

双击`起一个有趣的名字.docx`即可，名字可以起的吸引人有针对性

注意，文件的顺序：

```
Lucky_fishing
├── 其他资料
└── 起一个有趣的名字.docx.lnk
```
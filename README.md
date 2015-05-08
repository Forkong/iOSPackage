### iOS批量编译输出渠道包
#### 背景
最近朋友公司的app渠道变多了，每个渠道包基本没有太多差异，只要更换一下图片和渠道号就行。
如果手动打的话，实在太繁琐了，所以，我就帮他写了个Python脚本
（主要是我Python比较水，找机会练手）

#### 工程目录结构
工程目录结构主要类似于下面：
.
├── ArcTest
│   ├── ArcTest
│   ├── ArcTest.xcodeproj
│   ├── ArcTestTests
│   └── build
├── IPA
│   └── PP
├── MultiChannels
│   ├── 91
│   ├── AppStore
│   ├── HAIMA
│   ├── HULU
│   ├── KuaiYong
│   ├── PP
│   ├── TongBuTui
│   ├── XY
│   └── iTools
└── build.py

1. ArcTest:工程目录
2. MultiChannels:多渠道文件，里面包含需要替换的图片和包含渠道名称和渠道号的plist文件
.
├── 91
│   ├── Channel.plist
│   ├── default_splash_1134@2x.png
│   ├── default_splash_1908@3x.png
│   ├── default_splash_760@2x.png
│   └── default_splash_936@2x.png
├── AppStore
│   ├── Channel.plist
│   ├── default_splash_1134@2x.png
│   ├── default_splash_1908@3x.png
│   ├── default_splash_760@2x.png
│   └── default_splash_936@2x.png
3. build.py:批量打包使用的python文件
4. IPA:最后打包生成的文件目录，里面包含各个渠道的文件夹，各渠道文件夹内包含生成的.app .dSYM .ipa文件

#### build.py
主要过程就是：
1. 替换文件
2. clean
3. 编译
4. copy文件到IPA目录
5. 生成.ipa文件
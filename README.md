<h3>iOS批量编译输出渠道包</h3>

<h4>背景</h4>

<p>最近朋友公司的app渠道变多了，每个渠道包基本没有太多差异，只要更换一下图片和渠道号就行。</p>

<p>如果手动打的话，实在太繁琐了，所以，我就帮他写了个Python脚本</p>

<p>（主要是我Python比较水，找机会练手）</p>

<h4>工程目录结构</h4>

<p>工程目录结构主要类似于下面：</p>

<pre><code>.
├── ArcTest
│&nbsp;&nbsp; ├── ArcTest
│&nbsp;&nbsp; ├── ArcTest.xcodeproj
│&nbsp;&nbsp; ├── ArcTestTests
│&nbsp;&nbsp; └── build
├── IPA
│&nbsp;&nbsp; └── PP
├── MultiChannels
│&nbsp;&nbsp; ├── 91
│&nbsp;&nbsp; ├── AppStore
│&nbsp;&nbsp; ├── HAIMA
│&nbsp;&nbsp; ├── HULU
│&nbsp;&nbsp; ├── KuaiYong
│&nbsp;&nbsp; ├── PP
│&nbsp;&nbsp; ├── TongBuTui
│&nbsp;&nbsp; ├── XY
│&nbsp;&nbsp; └── iTools
└── build.py
</code></pre>

<ul>
	<li>ArcTest:工程目录</li>
	<li>MultiChannels:多渠道文件，里面包含需要替换的图片和包含渠道名称和渠道号的plist文件</li>
</ul>

<pre><code>.
├── 91
│&nbsp;&nbsp; ├── Channel.plist
│&nbsp;&nbsp; ├── default_splash_1134@2x.png
│&nbsp;&nbsp; ├── default_splash_1908@3x.png
│&nbsp;&nbsp; ├── default_splash_760@2x.png
│&nbsp;&nbsp; └── default_splash_936@2x.png
├── AppStore
│&nbsp;&nbsp; ├── Channel.plist
│&nbsp;&nbsp; ├── default_splash_1134@2x.png
│&nbsp;&nbsp; ├── default_splash_1908@3x.png
│&nbsp;&nbsp; ├── default_splash_760@2x.png
│&nbsp;&nbsp; └── default_splash_936@2x.png
</code></pre>

<ul>
	<li>build.py:批量打包使用的python文件</li>
	<li>IPA:最后打包生成的文件目录，里面包含各个渠道的文件夹，各渠道文件夹内包含生成的.app .dSYM .ipa文件</li>
</ul>

<h4>build.py</h4>

<p>主要过程就是：</p>

<ol>
	<li>替换文件</li>
	<li>clean</li>
	<li>编译</li>
	<li>copy文件到IPA目录</li>
	<li>生成.ipa文件</li>
</ol>
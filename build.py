#-*-coding:utf-8-*-
#!/usr/bin/python

import sys
import os
import shutil
import commands

channellist         = ['AppStore','91','PP', 'KuaiYong','TongBuTui','iTools', 'XY','HAIMA', 'HULU']
channelpath         = 'MultiChannels'
filenamelist        = ['Channel.plist','default_splash_760@2x.png','default_splash_936@2x.png','default_splash_1134@2x.png','default_splash_1908@3x.png']
filepathlist        = ['ArcTest/Channel.plist','ArcTest/default_splash_760@2x.png','ArcTest/default_splash_936@2x.png','ArcTest/default_splash_1134@2x.png','ArcTest/default_splash_1908@3x.png']
projectname         = 'ArcTest'
outputpath          = 'IPA/'

xcodebuildclean     = 'xcodebuild clean'
# release版本 需要调整对证书 否则打包时需要设置签名和证书
xcodebuildrelease   = 'xcodebuild -sdk iphoneos -configuration Release'
# debug版本
xcodebuilddebug     = 'xcodebuild -sdk iphonesimulator8.3 -configuration Debug'

# 替换文件
def replaceflies(channel):
	workspacepath = os.getcwd()
	srcpath = os.path.join(workspacepath, channelpath)
	srcpath = os.path.join(srcpath, channel)
	despath = os.path.join(workspacepath, projectname)
	# 替换资源
	for filename in filenamelist:
		index = filenamelist.index(filename)
		filepath = filepathlist[index]
		srcfullpath = os.path.join(srcpath, filename)
		desfullpath = os.path.join(despath, filepath)
		if os.path.exists(srcfullpath):
			shutil.copy(srcfullpath, desfullpath)
			print "Copy '" + srcfullpath + "' to '" + desfullpath + "'." 
		else:
			print "'" + srcfullpath + "'" + "不存在"

def move(buildmode, channel):
	buildpath = ''
	if buildmode == xcodebuilddebug:
		buildpath = projectname+'/build/Debug-iphonesimulator'
	else:
		buildpath = projectname+'/build/Release-iphoneos'

	outputfiletree = outputpath+channel
	if os.path.exists(outputfiletree):
		shutil.rmtree(outputfiletree)

	shutil.copytree(buildpath, outputfiletree)	

def clean():
	status ,output = commands.getstatusoutput('cd '+ projectname + '/;' + xcodebuildclean)
	print output

def build(buildmode):
	print '编译中，请稍等...'
	status ,output = commands.getstatusoutput('cd '+ projectname + '/;' + buildmode)
	print output
	
def transtoipa(buildmode, channel):
	print '生成ipa中...'
	apppath = outputpath+channel+'/'+'ArcTest.app'
	print apppath
	ipapath = os.getcwd()+'/'+outputpath+channel+'/'+'ArcTest.ipa'
	print ipapath
	status ,output = commands.getstatusoutput('xcrun -sdk iphoneos PackageApplication  -v '+apppath+' -o '+ipapath)
	print output

def main(argvs):
	if len(argvs) < 2:
		print "至少输入一个渠道名称"
		return
	else:
		for i in xrange(1,len(argvs)):
			channel = argvs[i]
			if not channel in channellist:
				print "没有此渠道名称"
			else:
				replaceflies(channel)
				# 先clean后编译
				clean()
				# 编译
				build(xcodebuildrelease)
				# 迁移出去
				move(xcodebuildrelease, channel)
				# 生成ipa包
				transtoipa(xcodebuildrelease, channel)
				


if __name__ == '__main__':
	# 外部输入 类似:
	# python build.py PP AppStore 91 KuaiYong TongBuTui
	main(sys.argv)

	# 内部设置
	# buildlist = ['AppStore','91']
	# main(buildlist)

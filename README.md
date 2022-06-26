# SimpleLipSync
通过语音驱动嘴型，输出BlenderShape 52keys，当前使用了5个表情，即"jawOpen", "mouthFunnel","mouthPucker", "mouthRollUpper", "mouthRollLower"



<video id="video" controls="" preload="none">
      <source id="mp4" src="https://user-images.githubusercontent.com/108171388/175798477-f57b6272-68e7-4a7c-9434-05763b734b0e.mp4" type="video/mp4">
      </video>

## 特点
1.实时预测，可用于直播场景

2.无需提供音素口型

3.即开即用

4.可运行于普通pc，无需GPU支持

5.输出可自行调节幅度大小

6.可直接应用于UE

## 说明
本项目运行于windows平台

测试脚本test_script.py为调用dll的样例，主要为了方便使用pyaudio调取麦克风数据

需安装pyaudio

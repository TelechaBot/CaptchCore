# CaptchCore

识别核心，自动生成题目文本，简单易用

## 调用说明

```python
# 意思就是从模块文件夹调用模块文件，然
import CaptchaCore
some = CaptchaCore.Importer().pull(difficulty_limit=5,model_name="数学题库")
print(some)
```
## 注意

每次创建一次都会重新生成问题。

## 效果示例
```
('一个球的半径为33，求其体积!(四舍五入，只答出数字部分！)', 47916)
一个球的半径为9，求其体积!(四舍五入，只答出数字部分！)
12348
```

## 关于 GTTS 验证

有关 GTTS 的验证不可用至商业项目中。
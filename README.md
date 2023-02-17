> # **Playfair古典加密实现**

Playfair（普莱费尔密码）是一种使用一个关键词方格来加密字符对的加密法，1854年由一位名叫[查尔斯·惠斯通](https://baike.baidu.com/item/查尔斯·惠斯通/10168121?fromModule=lemma_inlink)（Charles Wheatstone）的英国人发明。在1854到1855年的克里米亚战争和1899年的布尔战争中有广泛应用。但在1915年的一战中被破译了。

Playfair编写由明文、密钥、密文构成。

> ### 明文
**其中明文长度必须为偶数**。若其明文长度为奇数，则需在末尾添加字符 ‘X’ (或 ‘Q’ )，使其变为偶数。

> ### 密钥
> 密钥无多要求，不过**密钥字符越多样越好**。密钥中的字符“ I ”与“ J ”视为一个字符

> ### 密文 
> 密文是由明文经过和密钥的加工得到，不过其**长度和明文长度一致**，这是古典加密的普遍缺点。

下面开始分析Playfair加密过程，假设其密钥为” PlayfairPassword “。首先把密钥重复字符去除，就可以得到一串密钥” PLAYFIRSWOD ”

然后构建一个5x5的矩阵数列，将处理好的密钥以由上至下、由左至右的方向依次置入矩阵栅格内，就能得到以下的列表。
![passkey1](.\img\passkey.01.png)

然后将26个拉丁字母表，以字母表的顺序排列。去除在密钥中已出现的字符，同时也是将“ I ”和“ J ”视为同一字符。完成之后也同上面一样将其依次置入矩阵栅格内，如下
![passkey2](.\img\passkey.02.png)

> ### 加密

将矩阵和密钥准备好了。接下来就是加密工作了。假设明文为“ I can eat glass  it does not hurt me ”。首先去除空格，但是这个明文长度为奇数，所以在字符串后面加上“ X ”，得到了处理后的明文“ ICANEATGLASSITDOESNOTHURTMEX ”。

随后再将处理后的明文进行长度为2的切割处理，这样就得到了“ IC AN EA TG LA SS IT DO ES NO TH UR TM EX ”这组分段。
> 利用密钥矩阵对明文段落进行相对应的加密处理

1. 分段里**第一字符与第二字符平行时，其同时向右偏移一格得到密文，若出现字符于右末端无法向右偏移则穿透到同行左末端**，例如加密“ BG ”，如下
  
  ![entry1](./img/encry.01.png)

  得到密钥“ CD ”

~~~text
绿色栅格为明文字符，橙色栅格为密文字符，叠加颜色则既是明文字符亦是其他字符的密文字符
~~~

2. 分段里**第一字符与第二字符垂直时，其同时向下偏移一格得到密文，若出现字符于底端无法向下偏移则穿透到同列顶端**，例如加密“ TH ”，如下
  
  ![encry2](./img/encry.02.png)

  得到密钥“ PT ”

~~~text
绿色栅格为明文字符，橙色栅格为密文字符，叠加颜色则既是明文字符亦是其他字符的密文字符
~~~

3. 分段里**第一字符与第二字符既不平行也不垂直时，第一字符取其同一列而第二字符行的字符，第二字符则取其同列而第一字符行的字符，得到密钥**，例如加密“ NO ”，如下
  
  ![encry3](./img/encry.03.png)

  得到密钥“ WQ ”

~~~text
绿色栅格为明文字符，橙色栅格为密文字符，叠加颜色则既是明文字符亦是其他字符的密文字符
~~~

4.分段里**第一字符与第二字符相同时，则同时向下平移一位，若出现字符于底端无法向下偏移则穿透到同列顶端，得到密钥**，例如加密 “ SS ”，如下
  
  ![encry4](./img/encry.04.png)

得到密钥“ CC ”

~~~text
绿色栅格为明文字符，橙色栅格为密文字符，叠加颜色则既是明文字符亦是其他字符的密文字符
~~~

然后按照这种加密规则就可以把明文“ I can eat glass  it does not hurt me ”加密为密文“ D smy ycd zaycc dp i(j)gwc wqp tlbh vny ”。解密只需要拥有密钥矩阵做逆向操作即可。




> ## 利用Python实现Playfair对文件进行加密

文件或文本信息在十六进制编码下长度是偶数的，而且16进制字符长度也是4²，可以利用这点构建一个4x4的矩形数列。这样就满足了Playfair加密的所有条件，所以我尝试使用Python语言来实现普莱费尔加密

[跳转源码](https://github.com/KuromiNote/Playfair_python/blob/main/playfair.py)

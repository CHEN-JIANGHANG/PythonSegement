#python分词
##函数
- getNumber
	>从文件取数并且进行分析统计然后存到数据库中
- multythreadtest
	> 尝试多线程，但是后来莫名的提速了，之后放弃，数据量大的时候可以考虑
	> 目前的速度：240s完成1000条
- originSegementFunction
	>接受文本和分词方式并且返回分词结果，格式为json
- totalOperation
	>从数据库中取文本，进行分词并且写入到文本，格式为weiboid，userid，分词结果

分词的格式见工大[语言云](http://http://www.ltp-cloud.com/intro/)
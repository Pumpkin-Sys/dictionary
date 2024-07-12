# dictionary
这个工具实现了一个简单的目录爆破功能，用于检测网站上是否存在特定的目录或文件。以下是工具的主要功能概述：
读取字典内容 (dictionary1 函数)：
这个函数接收一个文件路径作为参数，读取该文件，并返回一个列表，其中包含了文件中的每一行数据，每行数据的末尾换行符被去除。
URL拼接并请求 (url 函数)：
接收基础URL和字典列表作为参数。
遍历字典中的每个条目，将其添加到基础URL后面形成完整的URL。
使用requests.get()发送HTTP GET请求到每个URL。
检查响应的状态码，如果状态码为200（成功）、302（临时重定向）或403（禁止访问），则认为URL可以访问，并将结果记录为“成功访问”，否则记录为“访问失败”。
主函数 (main 函数)：
提示用户输入要检测的URL和字典文件的路径。
调用dictionary1函数读取字典文件。
调用url函数进行URL拼接和请求处理。
调用save_to_txt函数将所有“成功访问”的URL保存到一个文本文件中。
打印所有的结果。
保存结果到TXT文件 (save_to_txt 函数)：
接收结果列表作为参数。
将所有标记为“成功访问”的URL写入名为pkn.txt的文件中。
当运行此工具时，它会要求用户提供一个目标URL和一个包含潜在目录或文件名称的字典文件路径。然后，它会尝试访问这些URL，并报告哪些URL是可访问的，同时将这些成功的URL保存到本地文件中。
这在安全审计和渗透测试中是有用的，但使用时应确保遵守相关法律法规和道德规范。

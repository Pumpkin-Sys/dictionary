import requests
#读取字典内容
def dictionary1(file_path):
    """
    读取字典内容
    :param file_path:
    :return:
    """
    # 读取文件内容
    with open(file_path, "r") as file:
        # 去除换行符
        return [line.strip() for line in file]

#url拼接并请求
def url(base_url, dictionary):
    results = []
    for path in dictionary:
        url = f"{base_url}/{path}"
        # print(url)
        res = requests.get(url)
        # #状态码检查
        if res.status_code == 200 or res.status_code == 302 or res.status_code == 403:
            results.append([url,"成功访问"])
            # print(f"{url} 访问成功")
        else:
            results.append([url,"访问失败"])
            # print(f"{url} 访问失败")
    return results
#主函数
def main():
    base_url = input("请输入要访问的URL:")
    # base_url = "http://www.duomi.com"
    # file_path = "D:/range/dictionary/目录字典/PHP(1).txt"
    file_path = input("请输入要读取的字典文件路径:")
    dictionary = dictionary1(file_path)
    # print(dictionary)
    results = url(base_url, dictionary)
    save_to_txt(results)
    for result in results:
        print(result)
#将成功访问的链接保存到txt文件
def save_to_txt(results):
    with open("pkn.txt", "a") as file:
        for result in results:
            # print(result[1])
            if result[1] == "成功访问":
                file.write(result[0] + "\n")

#运行主函数
if __name__ == "__main__":
    main()

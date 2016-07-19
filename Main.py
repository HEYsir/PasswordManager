import os

def Save():
        print("欢迎使用密码保存功能")
        pwInfo = []
        pwInfo.append(input("网站："))
        pwInfo.append(input("账户："))
        pwInfo.append(input("密码："))
        pwInfo.append(input("备注："))
        print(pwInfo)
        RunPath = os.getcwd()
        fp = open(RunPath+'\pw.csv','a+')     #如果文件不存在则创建文件
        seq = ","
        fp.write(seq.join(pwInfo))
        fp.write("\n")
        fp.close()

def main():
        print("  [1]密码保存")
        print("  [2]密码修改")
        print("  [3]密码获取")
        print("  [4]密码生成")
        print("  [5]密码管理")
        print("  ESC退出")
        funselect = input("请选择使用功能：")
        if (funselect == '1'):
                Save()

if __name__ == "__main__":
        print("欢迎使用HEYsir‘s密码管理工具")
        main();
        
	

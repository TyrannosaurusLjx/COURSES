class NaiveBayesClassifier:
    def __init__(self) :
        self.classes = set() # 存储所有C_i类别
        self.classes_prob = dict() # 每个C_i出现的可能性
        self.condition_prob = dict() # 每个C_i在A下的条件概率
        self.P0 = 1 # 先验概率

    # 训练函数
    def fit(self, spam_data_matrix, ham_data_matrix):
        from math import log
        spam_dim = len(spam_data_matrix)
        ham_dim = len(ham_data_matrix)
        dim = spam_dim + ham_dim
        self.P0 = log(spam_dim / dim)

        for line in spam_data_matrix:
            self.classes.update(set(line))
        for line in ham_data_matrix:
            self.classes.update(set(line))

        # C_i总体概率 和 条件概率
        for word in self.classes:
            spamif = 0
            hamif = 0
            for line in spam_data_matrix:
                if word in line:
                    spamif += 1
            for row in ham_data_matrix:
                if word in row:
                    hamif += 1
            self.classes_prob[word] = (spamif + hamif) / dim
            self.condition_prob[word] = (spamif) / spam_dim
        class_prob_sum = sum(self.classes_prob.values())
        condition_prob_sum = sum(self.condition_prob.values())
        self.classes_prob = {key:value/class_prob_sum for key,value in self.classes_prob.items()}
        self.condition_prob = {key:value/condition_prob_sum for key,value in self.condition_prob.items()}

        spam_p = (spam_dim + ham_dim) / dim
        return spam_dim, self.classes_prob, self.condition_prob

    # 判断每一个行是不是一个spam
    def IsSpam(self,data_list):
        from math import log
        condition_prob = 0
        # 在计算条件概率时，添加平滑值（alpha）到分子和分母中
        alpha = 1  # laplace平滑参数
        dim = len(self.classes)
        for word in data_list:
            if word in self.classes:
                condition_prob += log((self.condition_prob[word] + alpha) / (self.classes_prob[word] + alpha * dim))

        P = self.P0 + condition_prob

        # 将1/2的对数概率作为阈值来判断是否为spam
        threshold = log(1/2)
        if P >= threshold:
            print(P)
            return True
        else:
            return False

        # 做总体预测
    def predict(self, data_matrix):
        total_dim = len(data_matrix)
        isspam = []
        for item in data_matrix:
            if self.IsSpam(item) == True:
                isspam.append(True)
            else:
                isspam.append(False)
        return isspam


class BayesFile:
    def __init__(self, pwd) :
        self.pwd = pwd
        self.excluded_words = set()
        self.load_excluded_words()

    def load_excluded_words(self):
        with open(self.pwd+"/excluded_words.txt","r",encoding="utf-8") as file:
            self.excluded_words = set(word.strip() for word in file.readlines())

    def process_file(self, file_path):
        # 读取文件并将文章分割成单词
        words = []
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()  # 简单地使用空格分割
        words = [word for word in words if word.lower() not in self.excluded_words]
        return words

    def build_matrix(self):
        from os import path
        SpamMatrix = []
        HamMatrix = []
        for i in range(1, 26):
            file_name = f'{i}.txt'
            file_path = path.join(self.pwd+"/email/spam", file_name)
            if path.isfile(file_path):
                words = self.process_file(file_path)
                SpamMatrix.append(words)
            file_path = path.join(self.pwd+"/email/ham", file_name)
            if path.isfile(file_path):
                words = self.process_file(file_path)
                HamMatrix.append(words)

        return SpamMatrix,HamMatrix

def detect():
    NBC = NaiveBayesClassifier()
    FileMatrix = BayesFile(pwd="/home/jxluo/ubuntu/WorkPlace/grade3/Computer-Simulations/Homeworks/hw02")

    FileMatrix.load_excluded_words()
    ham, spam = FileMatrix.build_matrix()

    NBC.fit(ham_data_matrix=ham, spam_data_matrix=spam)
    # 随机选择一些样本
    def choice():
        indexLst = []
        detect_file = []
        from random import choice
        for index in range(20):
            k = choice([0,1])
            index = choice(range(1,25))
            if k == 1:
                indexLst.append(True)
                detect_file.append(spam[index])
            else:
                indexLst.append(False)
                detect_file.append(ham[index])
        return detect_file, indexLst

    Matrix, lst = choice()
    result = NBC.predict(Matrix)
    RightNum = sum(1 if result[index] == lst[index] else 0 for index in range(len(lst)))
    ratio = RightNum/len(lst)
    return ratio

print("检测成功率:{:.2f}%".format(detect()*100))


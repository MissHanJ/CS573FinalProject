import web
from collections import deque
import numpy as np
urls = (
    '/index.html', 'index',
	'/fruit.csv', 'csv',
    '/try.html','try1',
    '/project.csv','projection_response',
    '/data.csv',"response_data",
    "/pca_data.csv","project_data",
)
app = web.application(urls, globals())

class index:
    def GET(self):
		with open(r"index.html",'r') as f:
			return f.read()

class csv:
	def GET(self):
		with open(r"fruit.csv",'r') as f:
			return f.read()

class try1():
    def GET(self):
        with open(r"try.html") as f:
            return f.read()

class projection_response():
    def GET(self):
        pass
class response_data():
    def GET(self):
        print "data",web.input()
        with open(r"data.csv") as f:
            return f.read()
class project_data():
    def GET(self):
        print "pca data",web.input()
        if web.input()["method"]=="pca":
            with open(r"data.csv") as f:
                head,data = self.to_nparray(f.read())
                project_data = self.fake_pca(data)
                return self.to_csvString(head,project_data)

    def to_nparray(self,data):
        lines = deque(data.strip().split('\n'))
        head = lines.popleft().split(',')
        data = np.array([i.split(',') for i in list(lines)],dtype=np.float32)
        return head,data
    def fake_pca(self,data):
        u,c,v = np.linalg.svd(data,full_matrices=False)
        c[1] = 0
        data = np.dot(u,np.dot(np.diag(c),v))
        return data
    def to_csvString(self,head,data):
        data_to_text = [",".join(map(str,i)) for i in data]
        return "\n".join([",".join(head),"\n".join(data_to_text)])
if __name__ == "__main__":
    app.run()

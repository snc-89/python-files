class Assessment:
    def __init__(self, marks, outOf, weight):
        self.marks = marks
        self.outOf = outOf
        self.weight = weight


    def weightedResult(self):
        return self.marks/self.outOf*(self.weight)

    
class Unit:
    def __init__(self, finalExam, assessment_list):
        self.finalExam = finalExam
        self.assessments = assessment_list
        
    def assessmentTotal(self):
        total = 0
        for item in self.assessments:
            total = total + item.weightedResult()
        return total

    def unitTotal(self):
        return self.assessmentTotal() + self.finalExam.weightedResult()
        
    def marksNeededInExam(self):
        self.HD = ((84.01 - self.assessmentTotal())/self.finalExam.weight)*100
        self.D = ((74.01 - self.assessmentTotal())/self.finalExam.weight)*100
        self.Cr = ((64.01 - self.assessmentTotal())/self.finalExam.weight)*100
        self.P = ((49.01 - self.assessmentTotal())/self.finalExam.weight)*100

        arr = []
        arr.append(str("%.2f" % self.P))
        arr.append(str("%.2f" % self.Cr))
        arr.append(str("%.2f" % self.D))
        arr.append(str("%.2f" % self.HD))

        for i in range(len(arr)):
            if float(arr[i]) > 100:
                arr[i] = "not possible"
            elif float(arr[i]) <= 0:
                arr[i] = "already achieved"
            else:
                arr[i] = arr[i] + "%"
        
        string = """you need:
    pass: {} 
    credit: {}
    distinction: {}
    high distinction: {}"""
        print(string.format(arr[0],arr[1],arr[2],arr[3]))








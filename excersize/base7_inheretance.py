class GradeProcessor:
    def __init__(self):
        self._total = 0
        self._count = 0
        
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, value):
        self._total = value
        
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, value):
        self._count = value
    
    @property
    def average(self):
        return self.total / self.count if self.count > 0 else 0

class ClassProcessor(GradeProcessor):
    
    def __init__(self, name):
        super().__init__()
        self._name = name
        
    @property
    def name(self):
        return self._name

    def calcurate_average(self, students):
        print(f"{self._name}の成績処理を開始します")
        for student, score in students.items():
            print(f"{student}: {score}")
            self.total += score
            self.count += 1
        print(f"{self.name}の平均点: {self.average:.2f}点")
        return self.average

class SchoolProcessor(GradeProcessor):
    
    def calcurate_average(self, classes):
        for cls_name, students in classes.items():
            class_processor = ClassProcessor(cls_name)
            self.total += class_processor.calcurate_average(students)
            self.count += 1
        print(f"学校全体の平均点: {self.average:.2f}点")
        return self.average

classes = {
    "1年A組": {"佐藤": 85, "鈴木": 92, "高橋": 78},
    "1年B組": {"田中": 88, "渡辺": 76, "山本": 90, "中村": 85},
    "1年C組": {"伊藤": 80, "山田": 83},
}

school_processor = SchoolProcessor()
school_processor.calcurate_average(classes)
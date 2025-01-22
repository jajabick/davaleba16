class student:
    
    def __init__(self, student_data):
        self.student_data = student_data
        
    def __str__(self):
        
        result = ""
        for key, value in self.student_data.items():
            result += f"{key}: {value}"
        return result

student_info = {"name " : "nika ", "lastname " : "gvariani ", "age " : 16, " personal number " : 19528551943, " grades " : "10 ", " time until 18 ": 18 - 16}
student = student(student_info)
print(student)

class student2:
    
    def __init__(self, student_data):
        self.student_data = student_data
        
    def __str__(self):
        
        result = ""
        for key, value in self.student_data.items():
            result += f"{key}: {value}"
        return result

student_info2 = {"name " : "ani ", "lastname " : "maisuradze ", "age " : 13, " personal number " : 80194752043, " grades " : "7 ", " time until 18 ": 18 - 13}
student2 = student2(student_info2)
print(student2)

class student3:
    
    def __init__(self, student_data):
        self.student_data = student_data
        
    def __str__(self):
        
        result = ""
        for key, value in self.student_data.items():
            result += f"{key}: {value}"
        return result

student_info3 = {"name " : "gio ", "lastname " : "davitashvili ", "age " : 17, " personal number " : 62375991738, " grades " : "3 ", " time until 18 ": 18 - 17}
student3 = student3(student_info3)
print(student3)
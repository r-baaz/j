class student:
     def __init__(self,name,rollno,dep,city):
            self.name=name
            self.rollno=rollno
            self.dep=dep
            self.city=city
     def display(self): 
         print("name:",self.name,"rollno:",self.rollno,"dep",self.dep,"city",self.city)

t=student("Arbaaz",8,"IT","Mumbai")
st.display()


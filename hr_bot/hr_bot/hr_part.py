class NewHRQuery(object):

    def __init__(self, title, skills=None, age=None, location=None):
        self.dreamtitle = title.lower()
        if skills:
            self.dreamskills = skills
        if age:
            self.dreamage = age
        if location:
            self.dreamlocation = location

    def __str__(self):
         pass

    def hr_sourcer(self):
        pass
        #TODO write a code that will select all the interesting candidates from DB

    def hr_sales(self):
        pass
        #TODO write a code that will return the info of potentially interesting candidates to the NLP part

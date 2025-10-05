class Nigeria():
    def capital(self):
        print("Abuja is the capital city of Nigeria")

    def language(self):
        print("Igbo is the most widely spoken")

    def type(self):
        print("Nigeria is Developing Country")

class USA():
    def capital(self):
        print("Washington D.C is the capital city of USA")

    def language(self):
        print("English is the most widely spoken")

    def type(self):
        print("USA is Developed Country")

obN=Nigeria()
obU=USA()

for country in (obN,obU):
    country.capital()
    country.language()
    country.type()
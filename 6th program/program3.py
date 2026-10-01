class Fine:
    def calculate(self, days):
        if days > 7:
            fine = (days - 7) * 10
        else:
            fine = 0
        print("Fine:", fine)

f = Fine()
f.calculate(10)

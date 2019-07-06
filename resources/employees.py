class Employees:
    personal_relief = 1408
    gross_salary = ''

    # constructor
    def __init__(self, basic_salary, benefits):
        self.b_salary = basic_salary
        self.benefits = benefits
        self.band_1 = self.b_salary - 12298
        self.band_2 = self.band_1 - 11586
        self.band_3 = self.band_2 - 11586
        self.band_4 = self.band_3 - 11586
        self.band_5 = self.b_salary - (12298 + 11586 + 11586 + 11586)

    def get_payee(self):
        if self.band_1 > 0:
            if self.band_2 > 0:
                if self.band_3 > 0:
                    if self.band_4 > 0:
                        return (12298 * 10/100 + 11586*15/100 + 11586*20/100 + 11586*25/100 + self.band_5 * 30/100) - self.personal_relief
                    else:
                        return (12298 * 10/100 + 11586*15/100 + 11586*20/100 + 11586*25/100) - self.personal_relief
                else:
                    return (12298 * 10/100 + 11586*15/100 + 11586*20/100) - self.personal_relief
            else:
                return (12298 * 10/100 + 11586*15/100) - self.personal_relief
        else:
            return (12298 * 10/100) - self.personal_relief

    def get_gross_salary(self):
        self.gross_salary = self.b_salary + self.benefits
        return self.gross_salary

    def get_nhif(self):
        if self.gross_salary <= 5999:
            return 150
        elif self.gross_salary <= 7999:
            return 300
        elif self.gross_salary <= 11999:
            return 400
        elif self.gross_salary <= 14999:
            return 500
        elif self.gross_salary <= 19999:
            return 600
        elif self.gross_salary <= 24999:
            return 750
        elif self.gross_salary <= 29999:
            return 850
        elif self.gross_salary <= 34999:
            return 900
        elif self.gross_salary <= 39999:
            return 950
        elif self.gross_salary <= 44999:
            return 1000
        elif self.gross_salary <= 49999:
            return 1100
        elif self.gross_salary <= 59999:
            return 1200
        elif self.gross_salary <= 69999:
            return 1300
        elif self.gross_salary <= 79999:
            return 1400
        elif self.gross_salary <= 89999:
            return 1500
        elif self.gross_salary <= 99999:
            return 1600
        else:
            return 1700

    def get_net_salary(self):
        return self.gross_salary - self.get_payee() - self.get_nhif()

    def get_nssf(self):
        if self.gross_salary * 6/100 >= 6000:
            return 6000
        else:
            return self.gross_salary * 6/100








from tabulate import tabulate

class User:
    #Data User
    data_user = {
        1: ["Rosy", "Basic Plan", 12, 'rosy-123'],
        2: ["Ucok", "Premium Plan", 9, 'ucok-123'],
        3: ["Raka", "Standard Plan", 10, 'raka-123'],
        4: ["Adit", "Basic Plan", 24, 'adit-123'],
        5: ["Dinda", "Standard Plan", 20, 'dinda-123']
    }

    #Data List
    list_plan = ["Basic Plan", "Standard Plan", "Premium Plan"]
    list_benefit = [[True, True, True, 'Bisa Stream'],
                     [True, True, True, 'Bisa Download'],
                     [True, True, True, 'Kualitas SD'],
                     [False, True, True, 'Kualitas HD'],
                     [False, False, True, 'Kualitas UHD'],
                     [1, 2, 4, 'Number of Devices'],
                     ['3rd party Movie only', 'Basic Plan Content + Sports', 'Basic Plan + Standard Plan + PacFlix Original Series', 'Jenis Konten'],
                     [120_000, 160_000, 200_000, 'Harga']]
    headers = ['Basic Plan', 'Standard Plan', 'Premium Plan', 'Services']

    
    def __init__(self, username):
        """
        Fungsi ini digunakan untuk menginisialisasi objek user

        input: username(str)
        """
        self.username = username
        self.current_plan = None
        self.duration_plan = None
        self.kode_referral = None

        for key, value in self.data_user.items():
            if value[0] == self.username:
                self.current_plan = value[1]
                self.duration_plan = value[2]
                self.kode_referral = value[3]
                break

    def check_all_plan(self):
        """
        Fungsi ini digunakan untuk mencetak plan dan benefit

        input: None
        """
        print("List Benefit and Plan from PacFlix")
        print("")
        print(tabulate(self.list_benefit, self.headers))
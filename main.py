class Device:

    def init(self, device_type: str, vendor: str, model: str):
        self.device_type = device_type
        self.vendor = vendor
        self.model = model

    def __str__(self):
        return f"на складе {self.device_type} {self.vendor} {self.model}"


class Printer(Device):

    def __init__(self, vendor, model):
        super().init("принтер", vendor, model)


class Scaner(Device):

    def __init__(self, vendor, model):
        super().init("сканер", vendor, model)


class MFP(Printer, Scaner):
    """ МФУ - многофункциональное устройство (MFP - Multi-Function Printer) """

    def __init__(self, vendor, model, device_type="MFP"):
        super().__init__(vendor, model)
        self.device_type = device_type


printer_1 = Printer("HP", "Deskjet 2320")
print(printer_1)
Scaner_1 = Scaner("Canon", "LiDE300")
print(Scaner_1)
MFP_1 = MFP("Xerox", "3320DNI")
print(MFP_1)

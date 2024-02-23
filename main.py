import datetime

class Vehicle:
    def __init__(self, type, licenseplate):
        self.Type = type
        self.LicensePlate = licenseplate

class Ticket:
    def __init__(self, id):
        self.ID = id
        self.TimeIn = datetime.datetime(1, 1, 1)
        self.TimeOut = datetime.datetime(1, 1, 1)

class Receipt:
    def __init__(self, vehicle, ticket):
        self.Vehicle = vehicle
        self.TimeIn = datetime.datetime.now()
        self.TimeOut = datetime.datetime(1, 1, 1)
        ticket.TimeIn = self.TimeIn
        self.Ticket = ticket
        self.isLossTicket = False
        self.Total = 0.0

class ManageVehicles:
    def __init__(self, vehicleamount):
        self.ListVehicles = []
        self.ListTicket = []
        self.ListReceipt = []
        self.Turnovermotorbike = 0.0
        self.Turnoverbike = 0.0
        for i in range(vehicleamount):
            self.ListTicket.append(Ticket(i))

    def VehicleIn(self, vehicle):
        self.ListVehicles.append(vehicle)
        ticket = self.ListTicket[0]
        self.ListTicket.pop(0)
        self.ListReceipt.append(Receipt(vehicle, ticket))
        return ticket

    def VehicleOut(self, vehicle, ticket, vehicleinfo):
        dtn = datetime.datetime.now()
        if vehicle in self.ListVehicles:
            if ticket is None:
                save = len(self.ListReceipt)
                for i in range(len(self.ListReceipt) - 1, -1, -1):
                    if self.ListReceipt[i].Vehicle.LicensePlate == vehicleinfo and self.ListReceipt[i].TimeOut.year == 1:
                        save = i
                        break
                if save < len(self.ListReceipt):
                    passday = dtn.day - self.ListReceipt[save].TimeIn.day
                    if vehicle.Type == "motorbike":
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 3000 + passday * 35000 + 60000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 6000 + passday * 35000 + 60000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                    else:
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 2000 + passday * 15000 + 30000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 4000 + passday * 15000 + 30000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListReceipt[save].isLossTicket = True
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                else:
                    return None
            else:
                save = len(self.ListReceipt)
                for i in range(len(self.ListReceipt) - 1, -1, -1):
                    if self.ListReceipt[i].Vehicle.LicensePlate == vehicle.LicensePlate and self.ListReceipt[i].TimeOut.year == 1 and self.ListReceipt[i].Ticket.ID == ticket.ID:
                        save = i
                        break
                if save < len(self.ListReceipt):
                    passday = dtn.day - self.ListReceipt[save].TimeIn.day
                    if vehicle.Type == "motorbike":
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 3000 + passday * 35000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 6000 + passday * 35000
                            self.Turnovermotorbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                    else:
                        if dtn.hour < 18 and dtn.hour > 8:
                            self.ListReceipt[save].Total = 2000 + passday * 15000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        elif dtn.hour < 22 and dtn.hour >= 18:
                            self.ListReceipt[save].Total = 4000 + passday * 15000
                            self.Turnoverbike += self.ListReceipt[save].Total
                            self.ListReceipt[save].TimeOut = dtn
                            self.ListVehicles.remove(vehicle)
                            self.ListTicket.append(ticket)
                            return vehicle
                        else:
                            return None
                else:
                    return None
        else:
            return None

    def getAmountVehicle(self):
        return len(self.ListVehicles)

    def getTurnoverMotorbike(self):
        return self.Turnovermotorbike

    def getTurnoverBike(self):
        return self.Turnoverbike

    def getTurnover(self):
        return self.Turnovermotorbike + self.Turnoverbike

    def listVehiclelostTicket(self):
        listvehiclelostticket = []
        for receipt in self.ListReceipt:
            if receipt.isLossTicket:
                listvehiclelostticket.append(receipt.Vehicle)
        return listvehiclelostticket

    def getWarningVehicles(self):
        current_datetime = datetime.datetime.now()
        warning_vehicles = []

        for receipt in self.ListReceipt:
            entry_time = receipt.TimeIn
            vehicle_type = receipt.Vehicle.Type
            delta_days = (current_datetime - entry_time).days

            if (vehicle_type == "bike" and delta_days >= 3) or (vehicle_type == "motorbike" and delta_days >= 5):
                warning_vehicles.append(receipt.Vehicle)

        return warning_vehicles

    def getLostTicketsToday(self):
        current_datetime = datetime.datetime.now()

        start_time = current_datetime.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = current_datetime.replace(hour=22, minute=0, second=0, microsecond=0)

        lost_tickets = []

        for receipt in manage_vehicles.ListReceipt:
            if start_time <= receipt.TimeIn <= end_time:
                if receipt.isLossTicket:
                    lost_tickets.append(receipt.Vehicle)

        return lost_tickets

    def getDuplicateEntries(self):
        current_datetime = datetime.datetime.now()

        start_time = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
        end_time = current_datetime.replace(hour=23, minute=51, second=0, microsecond=999999)

        vehicles_in_day = {}
        duplicate_vehicles = []

        for receipt in self.ListReceipt:
            entry_time = receipt.TimeIn
            vehicle_license = receipt.Vehicle.LicensePlate

            if start_time <= entry_time <= end_time:
                if vehicle_license in vehicles_in_day:
                    vehicles_in_day[vehicle_license] += 1
                else:
                    vehicles_in_day[vehicle_license] = 1

                if vehicles_in_day[vehicle_license] == 2:
                    duplicate_vehicles.append(receipt.Vehicle)

        return duplicate_vehicles


managevehicles = ManageVehicles(100)
# vehicle1 = Vehicle("motorbike", "111")
# vehicle2 = Vehicle("bike", "222")
# vehicle3 = Vehicle("motorbike", "333")
# print(managevehicles.getAmountVehicle())
# ticket1 = managevehicles.VehicleIn(vehicle1)
#
# print(managevehicles.getAmountVehicle())
# ticket2 = managevehicles.VehicleIn(vehicle2)
# print(managevehicles.getAmountVehicle())
# vehicle11 = managevehicles.VehicleOut(vehicle1, ticket2, None)
# print(managevehicles.getAmountVehicle())
# vehicle11 = managevehicles.VehicleOut(vehicle1, ticket1, None)
# # print(vehicle11.LicensePlate)
# print(managevehicles.getAmountVehicle())
# print(managevehicles.getTurnover())
receipt1 = Receipt(Vehicle("bike", "ABC123"), Ticket(1))
receipt2 = Receipt(Vehicle("motorbike", "XYZ456"), Ticket(2))
receipt3 = Receipt(Vehicle("bike", "ABC123"), Ticket(3))

receipt1.TimeIn = datetime.datetime.now() - datetime.timedelta(days=0)
receipt2.TimeIn = datetime.datetime.now() - datetime.timedelta(days=5)
receipt3.TimeIn = datetime.datetime.now() - datetime.timedelta(days=0)

manage_vehicles = ManageVehicles(100)
manage_vehicles.ListReceipt.extend([receipt1, receipt2, receipt3])

warning_vehicles = manage_vehicles.getWarningVehicles()
for vehicle in warning_vehicles:
    print("Warning Vehicle:", vehicle.LicensePlate)

lost_tickets = manage_vehicles.getLostTicketsToday()
print("\nLost tickets today:")
for vehicle in lost_tickets:
    print(vehicle.LicensePlate)

duplicate_entries = manage_vehicles.getDuplicateEntries()
print("\nDuplicate entries in a day:")
for vehicle in duplicate_entries:
    print("License Plate:", vehicle.LicensePlate)



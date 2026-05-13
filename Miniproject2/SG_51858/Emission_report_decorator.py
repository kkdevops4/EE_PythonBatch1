class emission_report:
    def __init__(self, base_emission):
        self.base_emission = base_emission

            
    def get_emission(self):                             # method 
        return {
            "base_emission" : self.base_emission, 
            "Pollution_Index" : 0
        }
            
class emission_decorator:              # decorator-a thing that contains an mission report
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def get_emission(self):
        return self._wrapped.get_emission()
    

class CO2_decorator(emission_decorator):
    def get_emission(self):
        data = super().get_emission()                  # gets previous object's result from  parent class and extends it
        
        CO2 = data["base_emission"]*2.31
        
        data["CO2"] = round(CO2, 2)
        data["Pollution_Index"] += CO2
        
        return data
    
class NOx_decorator(emission_decorator):
    def get_emission(self):
        data = super().get_emission()
        
        NOx = data["base_emission"]*0.015
        
        data["NOx"] = round(NOx, 2)
        data["Pollution_Index"] += NOx * 10
        
        return data  
    
class PM_decorator(emission_decorator):
    def get_emission(self):
        data = super().get_emission()
        
        PM = data["base_emission"]*0.002
        data["PM"] = round(PM, 2)
        data["Pollution_Index"] += PM * 20
        
        return data
    
class risk_decorator(emission_decorator):
    def get_emission(self):
        data = super().get_emission()
        
        score = data["Pollution_Index"]
        
        if score <= 50:
            risk = "Low"
        elif score <= 100:
            risk = "Moderate"
        elif score <= 150:
            risk = "High"
        else:
            risk = "critical"
            
        data["risk_level"] = risk
        return data       
    
   
fuel = float(input("Enter fuel(Petrol) emission (liters): "))

report = risk_decorator(PM_decorator(NOx_decorator(CO2_decorator(emission_report(fuel)))))       # creating object


result = report.get_emission()                                                              # call "get_emission" method

    # print output
print("\n--- Emission Report ---")
print(f"Fuel Used: {result['base_emission']} L")
print(f"CO2: {result['CO2']} kg")
print(f"NOx: {result['NOx']} kg")
print(f"PM: {result['PM']} kg")
print(f"Pollution Index: {round(result['Pollution_Index'], 2)} ")
print(f"Risk Level: {result['risk_level']}")
    
print("\nNote: Assumed factors")

print("- NOx impact is 10× harmful than CO2.")
print("- PM impact is 20× harmful than CO2.")
print("Pollution_Index = CO2 + (NOx × 10) + (PM × 20)")
    
    
    
    
    

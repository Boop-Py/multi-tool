from pint import UnitRegistry



def temp(amount, temp_from, temp_to):

    ureg = UnitRegistry()
    Q_ = ureg.Quantity

    #temp 

    amount = 0
    unit_to_convert = "degC"
    ureg.unit_result_wanted = "degF"


    home = Q_(amount, ureg.unit_to_convert)
    temp = round(home.to(unit_result_wanted))
    print(str(unit_to_convert) + " is " + str(temp))
    return temp




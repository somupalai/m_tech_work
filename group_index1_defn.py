def gi(Ip, Wl):
    a = ""
    if gi >= 0:
        if ((Wl >= 0) and (Wl < 35)):
            a = "clay CL"
        elif ((Wl >= 35) and (Wl < 60)):
             a = "clay CI"
        else:
            a= "clay CH"
    else:
        if ((Wl>= 0) and (Wl< 60)):
            a =  "silt OI/MI"
        else:
            a= "silt OH/MH"
    return a
print gi(12,45)

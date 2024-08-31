import pandas as pd
import sklearn
import re


veh_info = pd.read_csv(r"include/vehicle_models.csv", delimiter = ";")


def formatting_column_names(df):
    
    col_dict = {x:re.sub("[-()/]","", x.lower().replace(" ","_").replace("__","_")) for x in df.columns }
    df.rename(columns=col_dict, inplace = True)
    
    return df

veh_info = formatting_column_names(veh_info)


selected_cols = ["make",
                 "year",
                 "drive",
                 "basemodel",
                 "model",
                 "engine_displacement",
                 "transmission",
                 "transmission_descriptor",
                 "vehicle_size_class",
                 "guzzler",
                 "t_charger",
                 "s_charger",
                 "atv_type",
                 "electric_motor",
                 "mfr_code",
                 "created_on",
                 "modified_on",
                 "annual_petroleum_consumption_for_fuel_type1",
                 "annual_petroleum_consumption_for_fuel_type2",
                 "city_gasoline_consumption",
                 "co2_fuel_type1",
                 "co2_fuel_type2",
                 "cylinders",
                 "engine_descriptor",
                 "annual_fuel_cost_for_fuel_type1",
                 "annual_fuel_cost_for_fuel_type2"
                 ]

veh_info = veh_info[selected_cols]
x_data = veh_info.drop("annual_petroleum_consumption_for_fuel_type1") 
y_data = veh_info.annual_petroleum_consumption_for_fuel_type1
veh_info_cat = veh_info.select_dtypes("object")
veh_info_num = veh_info.select_dtypes("number")

print(f"Numeric features: {veh_info_num.shape[1]}\nCategorical features:{veh_info_cat.shape[1]}\nTotal variables:{veh_info.shape[1]}")

#print(veh_info.columns.tolist())

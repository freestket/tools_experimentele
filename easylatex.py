import numpy as np

headers = ["A_1", "A_2", "A_3", "A_4"]
kol1 = ["a_11", "a_12", "a_13", "a_14", "a_15"]
kol2 = ["a_21", "a_22", "a_23", "a_24", "a_25"]
kol3 = ["a_31", "a_32", "a_33", "a_34", "a_35"]
kol4 = ["a_41", "a_42", "a_43", "a_44", "a_45"]
data = [kol1, kol2, kol3, kol4]

caption = "{Dit is de caption}"
label_string = "{tab:labeltje}"


columns = "{"
for i in range(len(data)):
    columns += "|c"
columns += "|}"
tabular_cmd = "{tabular}"



latex_table = ""
latex_table += "\\begin{table}[h!]\n"
latex_table += "\t\centering\n"
latex_table += f"\t\caption{caption}\n"
latex_table += f"\t\\begin{tabular_cmd}{columns}\n"
latex_table += "\t\t\hline\n"



headerline = "\t\t"
for i in range(len(headers)):
    headerline += headers[i]
    if i < len(headers) - 1:
        headerline += " & "
    else:
        headerline += " \\\\\n"
headerline += "\t\t\hline\hline\n"

latex_table += headerline



for i in range(len(data[0])):
    new_line = "\t\t"
    for col in data:
        new_line += col[i]
        if data.index(col) < data.index(data[len(data)-1]):
            new_line += " & "
        else:
            new_line += " \\\\\n"
            new_line += "\t\t\hline\n"
    latex_table += new_line



latex_table += "\t\end{tabular}\n"
latex_table += f"\t\label{label_string}\n"
latex_table += "\end{table}\n"

print(latex_table)
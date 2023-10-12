import pandas as pd
import json


def export (root):
    # Paso 1: Iterar sobre los nodos de anytree
    df = pd.DataFrame(columns=['Test_Name', 'Componente', 'Medición', 'Nominal', 'Limite Superior', 'Limite Inferior'])
    for batch in root.children:
        for btest in batch.children:
            for block in btest.children:
                test_name = block.data  # Asumiendo que la data del bloque es el nombre del test
                if block.children:
                    for child in block.children:
                        comp_name = child.name
                        measurement = child.data
                        limits = child.children[0].data.split("|") if child.children else []
                        
                        # Ajuste para los límites según su número
                        if len(limits) == 2:
                            nominal = None
                            upper_limit = limits[0]
                            lower_limit = limits[1]
                        elif len(limits) == 3:
                            nominal = limits[0]
                            upper_limit = limits[1]
                            lower_limit = limits[2]
                        else:
                            nominal, upper_limit, lower_limit = None, None, None
                        
                        df = df.append({
                            'Test_Name': test_name,
                            'Componente': comp_name,
                            'Medición': measurement,
                            'Nominal': nominal,
                            'Limite Superior': upper_limit,
                            'Limite Inferior': lower_limit
                        }, ignore_index=True)


    # Paso 2: Guardar el DataFrame en un archivo Excel
    with pd.ExcelWriter('resultados.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Resultados ICT", index=False)
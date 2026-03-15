def calcular_salario_neto(salario_base:float,bonificacion:float=0.0) -> float:
    descuento:float = salario_base*0.08
    salario_final:float =salario_base-descuento+bonificacion
    return salario_final
resultado_salario:float=calcular_salario_neto(3000000.0,5000.0)
print(f"El salario final es :${resultado_salario}")
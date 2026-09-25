compliance_ambiental = {
    "capacidade_total_frota": 50,
    "limite_ociosidade": 15,
    "percentual_minimo_carga": 0.30
}

def calcular_eficiencia_financeira(volume_final):
    limite_ociosidade = compliance_ambiental["limite_ociosidade"]

    if volume_final < limite_ociosidade:
        return "Alerta: Alto Custo de Ociosidade Detectado"

    return "Operacao dentro do limite de eficiencia"

import random
import pandas as pd
import xlsxwriter

Ks = [1, 2, 5, 10, 50, 100, 500, 1000] # Lista de valores de K

dados = [] # Lista para armazenar os dados

# Gera 10 execucoes comecando em 1
for i in range(1, 11):
    Porcentagem = random.randint(2, 100)  # P inteiro em %
    P = Porcentagem / 100
    linha = {"Iteração": i, "P (%)": Porcentagem}
    for K in Ks:
        S = 1 / ((1 - P) + (P / K))
        linha[f"K={K}"] = S
    dados.append(linha)

# Criar DataFrame
df = pd.DataFrame(dados)

# Criar arquivo Excel
arquivo = "amdahl_graficos.xlsx"
with pd.ExcelWriter(arquivo, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, float_format="%.5f", sheet_name="Resultados")
    workbook = writer.book
    worksheet_resultados = writer.sheets["Resultados"]

    worksheet_graficos = workbook.add_worksheet("Gráficos") # Criar aba para gráficos

    # Criar gráficos para cada iteração
    for idx, row in df.iterrows():
        iteracao = int(row["Iteração"])
        Porcentagem = row["P (%)"]

        chart = workbook.add_chart({"type": "line"}) # Criar gráfico do tipo linha

        chart.add_series({
            "name": f"P = {Porcentagem}%",
            "categories": ["Resultados", 0, 2, 0, len(Ks) + 1],  # cabeçalho K
            "values":     ["Resultados", idx + 1, 2, idx + 1, len(Ks) + 1],  # valores S
            "marker": {"type": "circle", "size": 6, "border": {"color": "black"}, "fill": {"color": "blue"}},
            "line": {"dash_type": "dash", "color": "blue"},  # linha pontilhada
        })

        chart.set_title({"name": f"It. {iteracao} - P = {Porcentagem}%"})
        chart.set_x_axis({"name": "K", "major_gridlines": {"visible": True, "line": {"dash_type": "dash"}}})
        chart.set_y_axis({"name": "S (Aceleração)", "major_gridlines": {"visible": True, "line": {"dash_type": "dash"}}})
        chart.set_legend({"position": "none"})

        # Inserir gráfico (2 por linha)
        row_pos = (idx // 2) * 15
        col_pos = (idx % 2) * 9
        worksheet_graficos.insert_chart(row_pos, col_pos, chart)

print(f"Arquivo Excel com gráficos salvo em: {arquivo}")
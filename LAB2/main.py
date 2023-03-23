import gradio as gr
import pandas as pd


def answer_tab(plik, w, dane):
    plk = pd.read_csv(plik)
    maxw, maxa = plk.shape

    w = int(w)
    if w <= 0 or w > maxw:
        tab = plk.head(w)
        ierror = 1
    else:
        tab = plk.head(w)
        ierror = 0

    maxo, maxa = tab.shape

    if ierror == 0:
        uwa = "BRAK UWAG"
    else:
        uwa = "PODANO NIEPRAWIDŁOWĄ ILOŚĆ WIERSZY"

    if dane == "(a) ile klas decyzyjnych" and ierror == 0:
        odpa = len(tab['Exited'].unique())
        odp = f"Liczba klas decyzyjnych: {odpa}"
    elif dane == "(b) wielkość każdej klasy decyzyjnej" and ierror == 0:
        odpb = tab['Exited'].value_counts().to_dict()
        odp = "Wielkość każdej klasy decyzyjnej: " + str(odpb)
    else:
        odp = "ERROR"

    if ierror == 0:
        ops = f'Tabela zawiera:\n- {maxo} obiektów\n - {maxa} atrybutów'
    else:
        ops = "ERROR"

    kls = f'{odp}'
    uwagi = f'{uwa}'

    return tab, ops, kls, uwagi


demo = gr.Interface(
    fn=answer_tab,
    inputs=[
        gr.inputs.Textbox(label="Nazwa pliku:", default="Churn_Modelling.csv"),
        gr.inputs.Number(label="Liczba wierszy:", default=1), gr.inputs.Dropdown(label="Odpowiada na pytanie:",
                                                                                 choices=["(a) ile klas decyzyjnych",
                                                                                          "(b) wielkość każdej klasy "
                                                                                          "decyzyjnej",
                                                                                          ""],
                                                                                 default="(a) ile klas decyzyjnych")
    ],
    outputs=[
        gr.outputs.Dataframe(label="Tabela", type='pandas'), gr.outputs.Textbox(label="Opis tabeli decyzyjnej"),
        gr.outputs.Textbox(label="Dodatkowe informacje:"), gr.outputs.Textbox(label="UWAGI:"),
    ],
)

demo.launch()

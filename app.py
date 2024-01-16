from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
import pandas as pd
from great_tables import GT


app_ui = ui.page_fluid(
    ui.input_file(id = "file1",
                  label = "Choose CSV File",
                  accept = [".csv", ".tsv", ".txt"],
                  multiple = False),
    ui.input_radio_buttons(id = "sep",
                           label = "Separator",
                           choices = ["Comma(,)", "Semicolon(;)", "Tab(\\t)"]),

    ui.input_radio_buttons(id = "quotechar",
                           label = "Quote Character",
                           choices= ["Double Quote(\")", "Single Quote(\')"]),

    ui.output_table("output_dataframe")
    )

def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.table

    # TODO: not able to render great table in shiny?

    def output_dataframe():

        # Seperator
        seperator = str(input.sep())
        if seperator == "Comma(,)":
            sep = ","
        elif seperator == "Semicolon(;)":
            sep = ";"
        else:
            sep = "\t"

        # Quote Character
        qc = str(input.quotechar())
        if qc == "Double Quote(\")":
            quotechar = "\""
        else:
            quotechar = "\'"

        file: list[FileInfo] | None = input.file1()
        if file is None:
            return pd.DataFrame()
        return pd.read_csv(file[0]["datapath"],
                           sep = sep,
                           quotechar = quotechar)
        # return GT(pd.read_csv(file[0]["datapath"]))

app = App(app_ui, server)
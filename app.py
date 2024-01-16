from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
import pandas as pd
from great_tables import GT


app_ui = ui.page_fluid(
    ui.input_file("file1", "Choose CSV File", accept=[".csv"], multiple=False),
    ui.output_table("output_dataframe")
    )

def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.table

    # TODO: not able to render great table in shiny?

    def output_dataframe():
        file: list[FileInfo] | None = input.file1()
        if file is None:
            return pd.DataFrame()
        return pd.read_csv(file[0]["datapath"])
        # return GT(pd.read_csv(file[0]["datapath"]))

app = App(app_ui, server)
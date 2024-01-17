from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
import htmltools
import shinyswatch
import pandas as pd
import great_tables as gt
import great_tables.shiny as gts


app_ui = ui.page_fluid(
    # thwmw for the app
    shinyswatch.theme.superhero(),

    ui.panel_title("Upload a CSV file",
                   window_title= "Accessible Data Visualization"),
    ui.input_file(id = "file1",
                  label = "",
                  accept = [".csv", ".tsv", ".txt"],
                  multiple = False),

    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_radio_buttons(id = "sep",
                                   label = ui.strong("Separator"),
                                   choices = ["Comma(,)", "Semicolon(;)", "Tab(\\t)"]),
            ui.tags.hr(),
            ui.input_radio_buttons(id = "quotechar",
                                   label = ui.strong("Quote Character"),
                                   choices= ["Double Quote(\")", "Single Quote(\')"])
        ),

        ui.panel_main(
            # gts.output_gt("output_dataframe")
            ui.output_data_frame("output_dataframe")
        )
    )
)

def server(input: Inputs, output: Outputs, session: Session):

    @output
    @render.data_frame
    # @gts.render_gt

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
            # return gt.GT(pd.DataFrame())
            return render.DataGrid(pd.DataFrame())
        
        data_frame = pd.read_csv(file[0]["datapath"],
                                 sep = sep,
                                 quotechar = quotechar,
                                 header = 0).reset_index()
        
        return render.DataGrid(data_frame,
                               filters = True)
    
        """ THIS PART IS FOR GREAT TABLES
        return (
            gt.GT(data = data_frame,
                  rowname_col="index")
            .tab_header(title = f"{file[0]['name']}",
                        subtitle = f"{data_frame.shape[1]} column(s) | {data_frame.shape[0]} row(s)")
            .tab_stubhead(label=gt.md("Index"))
        )
        """

app = App(app_ui, server)

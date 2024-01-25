from shiny import ui, render, App, Inputs, Outputs, Session, reactive
from shiny.types import FileInfo
from htmltools import css
import shinyswatch
import pandas as pd
import openpyxl, xlrd
import functions


app_ui = ui.page_navbar(
    # theme for the app
    shinyswatch.theme.darkly(),
    ui.nav_panel(
        "Instructions",
        ui.markdown(
            """
            This is an app for **Accessible Data Visualization**.

            Instructions to be added...
            """
        )
    ),

    # Step1: Upload a File
    ui.nav_panel(
        "Step 1",
        ui.panel_title(ui.tags.h3("Upload a File")),
                    # window_title= "Accessible Data Visualization"),
        ui.tags.br(),

        ui.card(
        ui.layout_sidebar(
            
            ui.sidebar(
                ui.input_selectize(id = "file_format",
                                label = ui.strong("File Format"),
                                choices = [".csv", ".tsv", ".xlsx"],
                                width = "100%"),

                # Add condition: if user selects ".csv" on file_format, they need to select separator/quote character
                # and only allowed to upload .csv file 
                ui.panel_conditional("input.file_format == '.csv'",
                                    functions.sep_input_radio_buttons(),
                                    ui.tags.hr(),
                                    functions.quotechar_input_radio_buttons(),
                                    ui.tags.hr(),
                                    functions.input_file(".csv")
                ),

                # Add condition: if user selects ".tsv" on file_format, they need to select quote character
                # and only allowed to upload .tsv file 
                ui.panel_conditional("input.file_format == '.tsv'",
                                    ui.tags.hr(),
                                    functions.input_file(".tsv")
                ),

                # Add condition: if user selects ".xlsx" on file_format, they are only allowed to upload .xlsx file 
                ui.panel_conditional("input.file_format == '.xlsx'",
                                    ui.input_text(id = "sheet_name",
                                                  label = ui.strong("Sheet Name"),
                                                  placeholder = "Type in sheet name...",),
                                    ui.tags.hr(),
                                    functions.input_file(".xlsx")
                ),  
            ),            

            ui.output_data_frame("output_dataframe"),

            open = "always",  
        ),

        height = "80vh",
        )    
    ),

    # Step2: Select Plot Types
    ui.nav_panel(
        "Step 2",
        ui.panel_title(ui.tags.h3("Select Plot Types")),

        ui.tags.br(),

        ui.card(
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_selectize(id = "plot_types",
                                       label = ui.strong("Plot Types"),
                                       choices = ["-------", "Line Plot", "Bar Plot", "Box Plot", "Histogram", "Scatter Plot"],
                                       selected = None,
                                       multiple = False)
                    ),
                
                ui.output_ui("plot_introductions"),
                open = "always",
            ),
        
        height = "80vh",
        ),
    ),
    
    # Step3: Select Columns
    ui.nav_panel(
        "Step 3",
        ui.panel_title(ui.tags.h3("Select Columns")),
    ),

    # Step4: Generate Plots
    ui.nav_panel(
        "Step 4",
        ui.panel_title(ui.tags.h3("Generate Plots")),
    ),
    title="Accessible Data Visualization",
)


def server(input: Inputs, output: Outputs, session: Session):
    
    @output
    @render.data_frame
    def output_dataframe():
        # Seperator
        if input.sep() == "Comma( , )":
            sep = ","
        elif input.sep() == "Semicolon( ; )":
            sep = ";"
        else:
            sep = "\t"

        # Quote Character
        if input.quotechar() == "Double Quote( \" )":
            quotechar = "\""
        else:
            quotechar = "\'"

        # Get file id
        file_id = functions.get_file_id(input.file_format())
        file_input = getattr(input, file_id)

        file: list[FileInfo] | None = file_input()
        if file is None:
            return render.DataGrid(pd.DataFrame())
        
        if file_id == "csv_file":
            data_frame = pd.read_csv(file[0]["datapath"],
                                        sep = sep,
                                        quotechar = quotechar,
                                        header = 0)\
                                    .reset_index()\
                                    .fillna("N/A")
            
        elif file_id == "tsv_file":
            data_frame = pd.read_table(file[0]["datapath"],
                                        sep = "\t",
                                        quotechar = quotechar,
                                        header = 0)\
                                    .reset_index()\
                                    .fillna("N/A")
            
        else:
            data_frame = pd.read_excel(file[0]["datapath"],
                                    sheet_name = input.sheet_name(),
                                    header = 0,
                                    engine = 'openpyxl')\
                                    .reset_index()\
                                    .fillna("N/A")
            
        return render.DataGrid(data_frame,
                                filters = True)

    
    @output
    # @render.text
    @render.ui
    def plot_introductions():
        if input.plot_types() == "-------":
            return ui.markdown(
                """
                Please select a plot type.
                """)
        
        elif input.plot_types() == "Line Plot":
            return (ui.markdown(
                """
                #### **Line Plot:**
                
                A line plot, also known as a line graph, is a type of chart that displays data points on a two-dimensional plane. It is particularly useful for showing trends and changes in data over a continuous interval or time period. In a line plot, data points are connected with straight lines, forming a continuous line that represents the overall trend.
                """
                ),

                ui.tags.hr(),

                ui.markdown(
                """
                #### **Instructions:**
                If you would like to create a line plot, please select:
                 - one column for `x-axis` (typically represents independent variable such as time or categories)
                 - one column for `y-axis` (typically represents dependent variable which is the data being measured)
                """))
        
        elif input.plot_types() == "Bar Plot":
            return (ui.markdown(
                """
                #### **Bar Plot:**
                A bar plot, also known as a bar chart or bar graph, is a graphical representation of categorical data in the form of rectangular bars. Each bar's length or height corresponds to the frequency or value of the data it represents. Bar plots are commonly used to compare and display the distribution of categorical variables.
                """
                ),

                ui.tags.hr(),

                ui.markdown(
                """
                #### **Instructions:**
                If you would like to create a bar plot, please select:
                 - one categorical column for `x-axis` (typically represents the categories or groups of the data)
                """))
        
        elif input.plot_types() == "Box Plot":
            return (ui.markdown(
                """
                #### **Box Plot:**
                A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. It provides a summary of key statistical measures and displays the spread and central tendency of the data. The plot is particularly useful for comparing the distribution of different groups or datasets.
                
                Here are the components of a box plot:
                1. `Box`: The box represents the interquartile range (IQR), which is the middle 50% of the data. The top and bottom edges of the box correspond to the first quartile (Q1) and third quartile (Q3), respectively. The length of the box thus indicates the spread of the central 50% of the data.
                2. `Line` (whisker): Lines (whiskers) extend from the top and bottom of the box to indicate the range of the data. These lines can extend to a certain distance (often 1.5 times the IQR) beyond the quartiles or may represent the minimum and maximum values within that range.
                3. `Median` (line inside the box): A line inside the box represents the median (Q2) of the dataset, which is the middle value when the data is ordered.
                4. `Outliers`: Individual data points beyond the whiskers may be considered outliers and are often plotted individually.
                """
                ),

                ui.tags.hr(),

                ui.markdown(
                """
                #### **Instructions:**
                If you would like to create a box plot, please select:
                 - one numerical column (containing the  data for which you want to see the distribution)
                """))

        elif input.plot_types() == "Histogram":
            return (ui.markdown(
                """
                #### **Histogram:**
                A histogram is a graphical representation of the distribution of a continuous dataset. It is used to visualize the underlying frequency distribution of a set of continuous or interval data. Histograms provide insights into the shape, center, and spread of the data.
                """
                ),

                ui.tags.hr(),

                ui.markdown(
                """
                #### **Instructions:**
                If you would like to create a histogram, please select:
                 - one numerical column for `x-axis`(containing the  data for which you want to see the distribution)
                """))

        else:
            return (ui.markdown(
                """
                #### **Scatter Plot:**
                A scatter plot is a type of data visualization that displays individual data points on a two-dimensional graph. It is particularly useful for showing the relationship between two continuous variables. Each point on the scatter plot represents a unique observation or data point, and the position of the point is determined by the values of the two variables being compared.
                """
                ),

                ui.tags.hr(),

                ui.markdown(
                """
                #### **Instructions:**
                If you would like to create a scatter plot, please select:
                 - one numerical column for `x-axis`(typically represents independent variable)
                 - one numerical column for `y-axis`(typically represents dependent variable)
                """))
app = App(app_ui, server)

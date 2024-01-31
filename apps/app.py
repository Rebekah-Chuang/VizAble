import functions
import openpyxl
import pandas as pd
import shinyswatch
import xlrd
from htmltools import css
from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req
from shiny.types import FileInfo

app_ui = ui.page_navbar(
  # theme for the app,
  shinyswatch.theme.darkly(),

  # Instructions:
  ui.nav_panel(
      "Instructions",
      ui.markdown(
          """
          This is an app for **Accessible Data Visualization**.
    
          Instructions to be added...
          """ 
      ),
  ),
  
  # Step1: Upload a File,,
  ui.nav_panel(
      "Step 1",
      ui.panel_title(ui.tags.h3("Upload a File")),
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
                                       functions.input_file(".csv"),
                  ),
                  
                  # Add condition: if user selects ".tsv" on file_format, they need to select quote character
                  # and only allowed to upload .tsv file 
                  ui.panel_conditional("input.file_format == '.tsv'",
                                       ui.tags.hr(),
                                       functions.input_file(".tsv"),
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
              
              ui.output_data_frame("get_output_df"),
              open = "always",  
          ),
        height = "80vh",
      )    
  ),

  # Step2: Check datatypes:
  ui.nav_panel(
      "Step 2",
      ui.panel_title(ui.tags.h3("Check datatypes for columns")),
      ui.tags.br(),
      ui.layout_sidebar(
          ui.sidebar(
              ui.input_selectize(id = "column_to_convert",
                                 label = ui.strong("Column"),
                                 choices = [],
                                 selected = None,
                                 multiple = False),
              ui.input_selectize(id = "convert_dtype",
                                 label = ui.strong("Convert to"),
                                 choices = ["Select an option", "str", "int", "float"],
                                 selected = None,
                                 multiple = False),

              ui.input_action_button(id = "convert",
                                     label = "Convert",
                                     class_ = "btn-success"),
              ),
          
          ui.layout_columns(
              ui.div(
                  ui.tags.h5("Original Datatypes"),
                  ui.tags.hr(),
                  ui.output_data_frame("get_output_dtypes_df")
              ),
              
              ui.div(
                  ui.tags.h5("Updated Datatypes"),
                  ui.tags.hr(),
                  ui.output_data_frame("get_updated_output_dtypes_df"),
              ),
              
              col_widths={"sm": (5, 5)},
          ),
          
          height = "80vh",
      ),
  ),

  # Step3: Select Plot Types:
  ui.nav_panel(
      "Step 3",
      ui.panel_title(ui.tags.h3("Select Plot Types")),
      ui.tags.br(),
      ui.card(
          ui.layout_sidebar(
              ui.sidebar(
                  ui.input_selectize(id = "plot_types",
                                     label = ui.strong("Plot Types"),
                                     choices = [],
                                     selected = None,
                                     multiple = False)
              ),
              
              ui.output_ui("get_plot_introductions"),
              open = "always",
          ),
          
          height = "80vh",
      ),
  ),
  
  # Step4: Select Columns:
  ui.nav_panel(
      "Step 4",
      ui.panel_title(ui.tags.h3("Select Columns")),
      ui.tags.br(),
      ui.card(
          ui.layout_sidebar(
              ui.sidebar(
                  # Add condition: if user selects "Line Plot" on plot_types
                  ui.panel_conditional("input.plot_types == 'Line Plot'",
                                       # add dropdown for x-axis and y-axis
                                       functions.xaxis_input_selectize("line"),
                                       ui.tags.hr(),
                                       functions.yaxis_input_selectize("line"),
                  ),
                  
                  ui.panel_conditional("input.plot_types == 'Bar Plot'",
                                       # add dropdown for x-axis
                                       functions.xaxis_input_selectize("bar"),
                  ),
                  
                  ui.panel_conditional("input.plot_types == 'Box Plot'",
                                       # add dropdown for x-axis
                                       functions.xaxis_input_selectize("box"),
                  ),
                  
                  ui.panel_conditional("input.plot_types == 'Histogram'",
                                       # add dropdown for x-axis
                                       functions.xaxis_input_selectize("hist"),
                  ),
                  
                  ui.panel_conditional("input.plot_types == 'Scatter Plot'",
                                       # add dropdown for x-axis and y-axis
                                       functions.xaxis_input_selectize("scatter"),
                                       ui.tags.hr(),
                                       functions.yaxis_input_selectize("scatter"),
                  ),
                  
                  open = "always",
              ),
              
              ui.output_data_frame("get_output_selected_cols"),
              height = "80vh",
          ),
      ),
  ),
  
  # Step5: Generate Plots:
  ui.nav_panel(
      "Step 5",
      ui.panel_title(ui.tags.h3("Generate Plots")),
      ui.tags.br(),
      ui.card(
          height = "80vh",
      ),
  ),
  
  title = "Accessible Data Visualization"
)


def server(input: Inputs, output: Outputs, session: Session):

    # Step 1: Upload a File
    reactive_df = reactive.Value(pd.DataFrame())

    @reactive.Effect
    def get_reactive_df():
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
            reactive_df.set(pd.DataFrame())
            return
        
        if file_id == "csv_file":
            data_frame = pd.read_csv(file[0]["datapath"],
                                     sep = sep,
                                     quotechar = quotechar,
                                     header = 0)
            
        elif file_id == "tsv_file":
            data_frame = pd.read_table(file[0]["datapath"],
                                       sep = "\t",
                                       quotechar = quotechar,
                                       header = 0)
            
        else:
            data_frame = pd.read_excel(file[0]["datapath"],
                                       sheet_name = input.sheet_name(),
                                       header = 0,
                                       engine = 'openpyxl')

        reactive_df.set(data_frame.reset_index().fillna("N/A"))
   
    @output
    @render.data_frame
    def get_output_df():
        data_frame = reactive_df.get()
        return render.DataGrid(data_frame, filters = True)
    
    @output
    @render.data_frame
    def get_output_df_head():
        data_frame = reactive_df.get()
        return render.DataGrid(data_frame.head(1))

    # Step 2: Check datatypes
    original_dtypes = {}
    reactive_dtypes_df = reactive.Value(pd.DataFrame())
    @reactive.Effect
    def get_reactive_dtypes_df():
        data_frame = reactive_df.get()

        if data_frame is not None and not data_frame.empty:
            data = {"Column Name": [],
                    "Data Type": []}
            
            for col in data_frame.columns.to_list():
                data["Column Name"].append(col)
                data["Data Type"].append(str(type(data_frame[col][0])))

                # Store the original data types in the dictionary
                original_dtypes[col] = str(type(data_frame[col][0]))

            dtypes_df = pd.DataFrame(data)
            reactive_dtypes_df.set(dtypes_df)

    @output
    @render.data_frame
    def get_output_dtypes_df():
        if not original_dtypes:
            return None
        
        # Create a data frame from the original_data_types dictionary
        original_dtypes_df = pd.DataFrame(original_dtypes.items(), columns=["Column Name", "Data Type"])
        return render.DataGrid(original_dtypes_df)

    @reactive.Effect
    def update_column_to_convert_selectize():
        choices = ["Select an option"] + reactive_df().columns.tolist()
        ui.update_selectize(id = "column_to_convert",
                            choices = choices,
                            selected = None) 

    @output
    @render.data_frame
    @reactive.event(input.convert)
    def get_updated_output_dtypes_df():
        print("The convert button is clicked.")
        data_frame = reactive_df.get()

        if data_frame is not None and not data_frame.empty:
            column_to_convert = input.column_to_convert()
            convert_dtype = input.convert_dtype()

            if column_to_convert == "Select an option":
                ui.notification_show("Please select a column to convert.")
            
            elif convert_dtype == "Select an option":
                ui.notification_show("Please select a data type to convert to.")

            elif column_to_convert != "Select an option" and convert_dtype != "Select an option":
                try:
                    updated_data_frame = data_frame.copy()
                    updated_data_frame[column_to_convert] = updated_data_frame[column_to_convert].astype(convert_dtype)
                    reactive_df.set(updated_data_frame)
                    ui.notification_show(f"Successfully converted column [{column_to_convert}] to type [{convert_dtype}].")

                except ValueError as e:
                    error_message = f"Failed to convert data in column '{column_to_convert}' to type '{convert_dtype}': {str(e)}"
                    ui.notification_show(error_message)
            
            data = {"Column Name": [],
                    "Data Type": []}
        
            for col in reactive_df.get().columns.to_list():
                data["Column Name"].append(col)
                data["Data Type"].append(str(type(reactive_df.get()[col][0])))
            
            updated_dtypes_df = pd.DataFrame(data)
            return render.DataGrid(updated_dtypes_df)

    # Step 3: Select Plot Types
    @reactive.Effect
    def update_plot_types_selectize():
        ui.update_selectize(id = "plot_types",
                            choices = ["Select an option", "Line Plot", "Bar Plot", "Box Plot", "Histogram", "Scatter Plot"],
                            selected = None)
        
    # Step 4: Select Columns
    @output
    @render.ui
    def get_plot_introductions():
        if input.plot_types() == "Line Plot":
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
                """
            ))
        
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
                """
            ))
        
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
                """
            ))

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
                """
            ))

        elif input.plot_types() == "Scatter Plot":
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
                """
            ))
        
        else:
            return (ui.markdown(
                """
                Please select a plot type.
                """
            ))
    
    @reactive.Effect
    def update_xaxis_selectize():
        choices = ['Select an option'] + reactive_df().columns.tolist()
        if input.plot_types() == "Line Plot":
            ui.update_selectize(id = 'line_x_axis',
                                choices = choices,
                                selected = None)
            ui.update_selectize(id = 'line_y_axis',
                                choices = choices,
                                selected = None)
        
        elif input.plot_types() == "Bar Plot":
            ui.update_selectize(id = 'bar_x_axis',
                                choices = choices,
                                selected = None)
        
        elif input.plot_types() == "Box Plot":
            ui.update_selectize(id = 'box_x_axis',
                                choices = choices,
                                selected = None)
        
        elif input.plot_types() == "Histogram":
            ui.update_selectize(id = 'hist_x_axis',
                                choices = choices,
                                selected = None)
        
        else:
            ui.update_selectize(id = 'scatter_x_axis',
                                choices = choices,
                                selected = None)
            ui.update_selectize(id = 'scatter_y_axis',
                                choices = choices,
                                selected = None)

    @output
    @render.data_frame
    def get_output_selected_cols():
        data_frame = reactive_df.get()
        if data_frame.empty:
            return
        
        if input.plot_types() == "Line Plot":
            req(input.line_x_axis(), input.line_y_axis())
            x_col = input.line_x_axis()
            y_col = input.line_y_axis()
            if x_col in data_frame.columns and y_col in data_frame.columns:
                selected_cols = data_frame[[input.line_x_axis(), input.line_y_axis()]]
            else:
                return pd.DataFrame()
        
        elif input.plot_types() == "Bar Plot":
            req(input.bar_x_axis())
            x_col = input.bar_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[input.bar_x_axis()]]
            else:
                return pd.DataFrame()
        
        elif input.plot_types() == "Box Plot":
            req(input.box_x_axis())
            x_col = input.box_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[input.box_x_axis()]]
            else:
                return pd.DataFrame()
        
        elif input.plot_types() == "Histogram":
            req(input.hist_x_axis())
            x_col = input.hist_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[input.hist_x_axis()]]
            else:
                return pd.DataFrame()
        
        elif input.plot_types() == "Scatter Plot":
            req(input.scatter_x_axis(), input.scatter_y_axis())
            x_col = input.scatter_x_axis()
            y_col = input.scatter_y_axis()
            if x_col in data_frame.columns and y_col in data_frame.columns:
                selected_cols = data_frame[[input.scatter_x_axis(), input.scatter_y_axis()]]
            else:
                return pd.DataFrame()
        
        return selected_cols

app = App(app_ui, server)

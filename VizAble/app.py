from VizAble import functions, introductions, upload_file, check_datatypes, select_plottypes, select_columns, generate_plots, chatbot
import pandas as pd
import shinyswatch
from htmltools import css
from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module, run_app
from shiny.types import FileInfo
from typing import Optional
from pandas.errors import ParserError
import plotly.express as px
from shinywidgets import output_widget, render_widget
import google.generativeai as genai
import os, configparser
import matplotlib.pyplot as plt
import seaborn as sns

app_ui = ui.page_navbar(
    # theme for the app,
    shinyswatch.theme.cosmo(),

    # Instructions:
    introductions.introductions_ui(),

    # Step1: Upload a File
    upload_file.upload_ui(),

    # Step2: Check datatypes:
    check_datatypes.check_datatypes_ui(),

    # Step3: Select Plot Types:
    select_plottypes.select_plottypes_ui(),

    # Step4: Select Columns:
    select_columns.select_columns_ui(),

    # Step5: Generate Plots:
    generate_plots.generate_plots_ui(),

    # Step6: Chatbot:
    chatbot.chatbot_ui(),

    title="VizAble - Accessible Data Visualization Tool",
    window_title="VizAble",
    lang="en",
)


def server(input: Inputs, output: Outputs, session: Session):
    file_check = reactive.value(False)
    reactive_df: reactive.Value[pd.DataFrame] = reactive.Value(pd.DataFrame())
    reactive_dtypes_df: reactive.Value[pd.DataFrame] = reactive.Value(pd.DataFrame())
    decoded_image: str = reactive.value(None)
    
    # Step 1: Upload a File
    @render.ui
    @reactive.event(file_check, input.file_format)
    def dynamic_file_input():
        if input.file_format() != "Select an option":
            return functions.input_file(input.file_format())

    @reactive.Effect
    @reactive.event(input.csv_file, input.sep, input.quotechar)
    def get_reactive_df_csv() -> None:
        """ Read the uploaded csv file and store it in a reactive value.
        """
        print("Before selecting csv file input...")  # Initial check to see if this gets called

        # Seperator
        sep: str
        if input.sep() == "Comma( , )":
            sep = ","
        elif input.sep() == "Semicolon( ; )":
            sep = ";"
        else:
            sep = "\t"

        # Quote Character
        quotechar: str
        if input.quotechar() == 'Double Quote( " )':
            quotechar = '"'
        else:
            quotechar = "'"

        # Get file id
        file_id: str = functions.get_file_id(input.file_format())
        if file_id:
            file_input = getattr(input, file_id)

            file: list[FileInfo] | None = file_input()
            if file is None:
                reactive_df.set(pd.DataFrame())
                return

            data_frame: pd.DataFrame

            if file_id == "csv_file":
                data_frame = functions.read_csv_file(file[0]["datapath"], sep, quotechar)
                reactive_df.set(data_frame)
                print("File processed, updating reactive_df...")  # Debugging statement

    @reactive.Effect
    @reactive.event(input.tsv_file)
    def get_reactive_df_tsv() -> None:
        """ Read the uploaded tsv file and store it in a reactive value.
        """
        print("Before selecting tsv file input...")  # Initial check to see if this gets called

        # Get file id
        file_id: str = functions.get_file_id(input.file_format())
        if file_id:
            file_input = getattr(input, file_id)

            file: list[FileInfo] | None = file_input()
            if file is None:
                reactive_df.set(pd.DataFrame())
                return

            data_frame: pd.DataFrame

            if file_id == "tsv_file":
                try: 
                    data_frame = pd.read_table(
                            file[0]["datapath"],
                            sep="\t",
                            quotechar="'",
                            header=0
                        )
                    reactive_df.set(data_frame.reset_index().fillna("N/A"))
                    print("File processed, updating reactive_df...")  # Debugging statement

                except Exception as e:
                    # catch the error and display it to the user
                    error_message = f"An error occurred while processing the file. Please ensure that the file format is correct and try again. Error: {str(e)}.\n Press Escape key or Dismiss button to close this message."
                    ui.modal_show(ui.modal(error_message,
                                            easy_close=True))
                    reactive_df.set(pd.DataFrame())

    @reactive.Effect
    @reactive.event(input.xlsx_file)
    def get_reactive_df_xlsx() -> None:
        """ Read the uploaded xlsx file and store it in a reactive value.
        """
        print("Before selecting xlsx file input...")  # Initial check to see if this gets called

        # Get file id
        file_id: str = functions.get_file_id(input.file_format())
        if file_id:
            file_input = getattr(input, file_id)

            file: list[FileInfo] | None = file_input()
            if file is None:
                reactive_df.set(pd.DataFrame())
                return

            data_frame: pd.DataFrame

            if file_id == "xlsx_file":
                sheet_names: list[str] = functions.get_excel_sheet_names(file[0]["datapath"])
                ui.update_select(
                    id="sheet_name",
                    choices=["Select an option"] + sheet_names,
                    selected=sheet_names[0] if sheet_names else None,
                )
                print("File processed, updating reactive_df...")  # Debugging statement

    @reactive.Effect
    @reactive.event(input.sheet_name)
    def update_excel_dataframe() -> None:
        """ Update the excel dataframe based on the selected sheet name.
        """
        file_id: str = functions.get_file_id(input.file_format())
        if file_id:
            file_input = getattr(input, file_id)

            file: list[FileInfo] | None = file_input()
            if file is None or not file:
                reactive_df.set(pd.DataFrame())
                return

            if file_id == "xlsx_file" and input.sheet_name():
                try:
                    data_frame = pd.read_excel(
                        file[0]["datapath"],
                        sheet_name=input.sheet_name(),
                        engine="openpyxl",
                    )
                    reactive_df.set(data_frame.reset_index().fillna("N/A"))

                except Exception as e:
                    # catch the error and display it to the user
                    error_message = f"An error occurred while processing the file. Please ensure that the file format is correct and try again. Error: {str(e)}.\n Press Escape key or Dismiss button to close this message."
                    ui.modal_show(ui.modal(error_message,
                                           easy_close=True))
                    reactive_df.set(pd.DataFrame())

    @render.data_frame
    def get_output_df() -> render.DataGrid:
        """ Render the data frame in a data grid based on the uploaded file.

        :return: A data grid to display the uploaded data frame.
        :rtype: render.DataGrid
        """
        if not reactive_df.get().empty:
            data_frame: pd.DataFrame = reactive_df.get()
            print(f"Rendering data frame, rows: {len(data_frame)}")  # Debugging statement
            return render.DataGrid(data_frame, row_selection_mode="multiple")
        else:
            print("Data frame is empty.")  # Confirm empty state handling
            return render.DataGrid(pd.DataFrame(), row_selection_mode="multiple")                
    
    @reactive.Effect
    @reactive.event(input.reset)
    def reset_selections() -> None:
        """ Reset users' selections(`file_format`, `sheet_name`), and uploaded file when the reset button is clicked.
        """
        ui.update_select(
            id="file_format",
            selected="Select an option",
        )
        ui.update_select(
            id="sheet_name",
            selected="Select an option",
        )
        ui.update_select(
            id="sep",
            selected=[]
        )
        ui.update_select(
            id="quotechar", 
            selected=[]
        )
        
        file_check.set(not file_check.get())
        reactive_df.set(pd.DataFrame())

    # Step 2: Check datatypes
    original_dtypes: dict[str, str] = {}
    @reactive.Effect
    @reactive.event(reactive_df)
    def get_reactive_dtypes_df() -> None:
        """ Get the data types of the columns in the uploaded data frame and store them in a reactive value.
        """
        data_frame = reactive_df.get()
        original_dtypes.clear()  # Clear existing entries in the dictionary

        if data_frame is not None and not data_frame.empty:
            # Repopulate the dictionary with current data types
            for col in data_frame.columns:
                original_dtypes[col] = str(type(data_frame[col][0]))

            # Generate the DataFrame for display based on the updated dictionary
            dtypes_df: pd.DataFrame = pd.DataFrame(list(original_dtypes.items()),
                                                   columns=["Column Name", "Data Type"])
            reactive_dtypes_df.set(dtypes_df)
        else:
            reactive_dtypes_df.set(pd.DataFrame(columns=["Column Name", "Data Type"]))

    @render.data_frame
    @reactive.event(reactive_df)
    def get_output_dtypes_df() -> Optional[render.DataGrid]:
        """ Render the data types of the columns in a data grid based on the uploaded file.

        :return: A data grid to display the data types of the columns in the uploaded data frame.
        :rtype: Optional[render.DataGrid]
        """
        if not original_dtypes:
            return None

        # Create a data frame from the original_data_types dictionary
        original_dtypes_df: pd.DataFrame = pd.DataFrame(original_dtypes.items(),
                                                        columns=["Column Name", "Data Type"])
        return render.DataGrid(original_dtypes_df,
                               width="100%")

    @reactive.Effect
    @reactive.event(reactive_df)
    def update_column_to_convert_select() -> None:
        """ Update the dropdown for users to select the column to convert based on the uploaded data frame.
        """
        choices: list[str] = ["Select an option"] + reactive_df().columns.tolist()
        ui.update_select(
            id="column_to_convert",
            choices=choices,
            selected=None
        )
    
    @reactive.Effect
    @reactive.event(reactive_df)
    def update_convert_dtype_select() -> None:
        """ Update the dropdown for users to select the data type to convert to based on the uploaded data frame.
        """
        choices: list[str] = ["Select an option", "str", "int", "float"]
        ui.update_select(
            id="convert_dtype",
            choices=choices,
            selected=None
        )

    @render.data_frame
    @reactive.event(input.convert)
    def get_updated_output_dtypes_df() -> Optional[render.DataGrid]:
        """ Render the updated data types of the columns in a data grid after data type conversion.

        :return: A data grid to display the updated data types of the columns after data type conversion.
        :rtype: Optional[render.DataGrid]
        """
        print("The convert button is clicked.")
        data_frame = reactive_df.get()

        if input.convert():
            if data_frame is not None and not data_frame.empty:
                column_to_convert: str = input.column_to_convert()
                convert_dtype: str = input.convert_dtype()

                if column_to_convert == "Select an option":
                    message = ui.modal("Message: Please select a column to convert. Press Escape key or Dismiss button to close this message.",
                                       easy_close=True)
                    ui.modal_show(message)

                elif convert_dtype == "Select an option":
                    message = ui.modal("Message: Please select a data type to convert to. \n Press Escape key or Dismiss button to close this message.",
                                       easy_close=True)
                    ui.modal_show(message)

                elif (column_to_convert != "Select an option" and convert_dtype != "Select an option"):
                    try:
                        updated_data_frame = data_frame.copy()
                        updated_data_frame[column_to_convert] = updated_data_frame[column_to_convert].astype(convert_dtype)
                        reactive_df.set(updated_data_frame)
                        message = ui.modal(f"Message: Successfully converted column [{column_to_convert}] to type [{convert_dtype}]. \n Press Escape key or Dismiss button to close this message.",
                                           easy_close=True)
                        ui.modal_show(message)

                    except ValueError as e:
                        error_message: str = f"Message: Failed to convert data in column '{column_to_convert}' to type '{convert_dtype}': {str(e)} \n Press Escape key or Dismiss button to close this message."
                        ui.modal_show(ui.modal(error_message,
                                               easy_close=True))

                data: dict = {"Column Name": [],
                            "Data Type": []}

                for col in reactive_df.get().columns.to_list():
                    data["Column Name"].append(col)
                    data["Data Type"].append(str(type(reactive_df.get()[col][0])))

                updated_dtypes_df: pd.DataFrame = pd.DataFrame(data)
                return render.DataGrid(updated_dtypes_df,
                                       width="100%")

    # Step 3: Select Plot Types
    @reactive.Effect
    @reactive.event(input.file_format, reactive_df, input.sheet_name)
    def update_plot_types_select() -> None:
        """ Update the dropdown for users to select the plot types based on the uploaded data frame.
        """
        data_frame = reactive_df.get()
        if data_frame is not None and not data_frame.empty:
            choices: list[str] = [
                "Select an option",
                "Line Plot",
                "Bar Plot",
                "Box Plot",
                "Grouped_Box Plot",
                "Histogram",
                "Scatter Plot"
            ]
        else:
            choices: list[str] = ["Select an option"]

        ui.update_select(
            id="plot_types",
            choices=choices,
            selected=None,
        )

    # Step 4: Select Columns
    @render.ui
    def get_plot_introductions():
        """ Get the introduction and instructions for the selected plot type.
        """
        if input.plot_types() == "Line Plot":
            return (
                ui.markdown(
                    """
                ## **Line Plot:**
                
                A line plot, also known as a line graph, is a type of chart that displays data points on a two-dimensional plane. It is particularly useful for showing trends and changes in data over a continuous interval or time period. In a line plot, data points are connected with straight lines, forming a continuous line that represents the overall trend.
                """
                ),
                ui.tags.hr(),
                ui.markdown(
                    """
                ## **Instructions:**
                If you would like to create a line plot, please select:
                 - one column for `x-axis` (typically represents independent variable such as time or categories)
                 - one column for `y-axis` (typically represents dependent variable which is the data being measured)
                """
                ),
            )

        elif input.plot_types() == "Bar Plot":
            return (
                ui.markdown(
                    """
                ## **Bar Plot:**
                A bar plot, also known as a bar chart or bar graph, is a graphical representation of categorical data in the form of rectangular bars. Each bar's length or height corresponds to the frequency or value of the data it represents. Bar plots are commonly used to compare and display the distribution of categorical variables.
                """
                ),
                ui.tags.hr(),
                ui.markdown(
                    """
                ## **Instructions:**
                If you would like to create a bar plot, please select:
                 - one categorical column for `x-axis` (typically represents the categories or groups of the data)
                """
                ),
            )

        elif input.plot_types() == "Box Plot":
            return (
                ui.markdown(
                    """
                ## **Box Plot:**
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
                ## **Instructions:**
                If you would like to create a box plot, please select:
                 - one numerical column (containing the  data for which you want to see the distribution)
                """
                ),
            )
        elif input.plot_types() == "Grouped_Box Plot":
            return (
                ui.markdown(
                    """
                ## **Grouped Box Plot:**
                A grouped box plot is a graphical representation that enables the comparison of distributions between multiple groups or categories within a dataset. It provides insights into the variability, central tendency, and spread of a variable across different groupings.

                Here are the components of a box plot:
                1. `Boxes`: Each box represents the interquartile range (IQR), which is the middle 50% of the data. The top and bottom edges of the box correspond to the first quartile (Q1) and third quartile (Q3), respectively. The length of the box thus indicates the spread of the central 50% of the data.
                2. `Line` (whisker): Lines (whiskers) extend from the top and bottom of the box to indicate the range of the data. These lines can extend to a certain distance (often 1.5 times the IQR) beyond the quartiles or may represent the minimum and maximum values within that range.
                3. `Median` (line inside the box): A line inside the box represents the median (Q2) of the dataset, which is the middle value when the data is ordered.
                4. `Grouping`: The boxes are grouped together, allowing for a visual comparison of the distribution of the variable across different groups. This facilitates the identification of differences or similarities in the data distribution between the groups.
                5. `Outliers`: Individual data points beyond the whiskers may be considered outliers and are often plotted individually.
                """
                ),
                ui.tags.hr(),
                ui.markdown(
                    """
                ## **Instructions:**
                If you would like to create a box plot, please select:
                 - one numerical column (containing the  data for which you want to see the distribution)
                 - one categorical column for `grouping` (to compare the distribution across different groups)
                """
                ), 
            )
        
        elif input.plot_types() == "Histogram":
            return (
                ui.markdown(
                    """
                ## **Histogram:**
                A histogram is a graphical representation of the distribution of a continuous dataset. It is used to visualize the underlying frequency distribution of a set of continuous or interval data. Histograms provide insights into the shape, center, and spread of the data.
                """
                ),
                ui.tags.hr(),
                ui.markdown(
                    """
                ## **Instructions:**
                If you would like to create a histogram, please select:
                 - one numerical column for `x-axis`(containing the  data for which you want to see the distribution)
                """
                ),
            )

        elif input.plot_types() == "Scatter Plot":
            return (
                ui.markdown(
                    """
                ## **Scatter Plot:**
                A scatter plot is a type of data visualization that displays individual data points on a two-dimensional graph. It is particularly useful for showing the relationship between two continuous variables. Each point on the scatter plot represents a unique observation or data point, and the position of the point is determined by the values of the two variables being compared.
                """
                ),
                ui.tags.hr(),
                ui.markdown(
                    """
                ## **Instructions:**
                If you would like to create a scatter plot, please select:
                 - one numerical column for `x-axis`(typically represents independent variable)
                 - one numerical column for `y-axis`(typically represents dependent variable)
                """
                ),
            )

        else:
            return ui.markdown(
                """
                Please select a plot type.
                """
            )

    @reactive.Effect
    def update_axis_select() -> None:
        """ Updates dropdown options for selecting the x-axis and optionally the y-axis, based on the uploaded data and the chosen plot type.
        """
        data_frame = reactive_df.get()
        choices: list[str] = functions.return_choices_for_columns(data_frame, input.plot_types())

        # update both x-axis and y-axis dropdowns
        if input.plot_types() in ["Line Plot", "Scatter Plot"]:
            functions.update_xaxis_input_select(input.plot_types(), choices)
            functions.update_yaxis_input_select(input.plot_types(), choices)
        
        # update only x-axis dropdowns
        elif input.plot_types() in ["Bar Plot", "Histogram"]:
            functions.update_xaxis_input_select(input.plot_types(), choices)
        
        # update only y-axis dropdowns
        elif input.plot_types() in ["Box Plot"]:
            functions.update_yaxis_input_select(input.plot_types(), choices)
        
        # update y-axis and grouping dropdowns
        elif input.plot_types() in ["Grouped_Box Plot"]:
            functions.update_yaxis_input_select(input.plot_types(), choices)
            functions.update_grouping_input_select(input.plot_types(), functions.return_choices_for_columns(data_frame, "Categorical"))
            
    @render.data_frame
    def get_output_selected_cols() -> pd.DataFrame:
        """ Display the selected columns after users' column selections.

        :return: A data frame containing the selected columns.
        :rtype: pd.DataFrame
        """
        data_frame = reactive_df.get()
        selected_cols: pd.DataFrame = pd.DataFrame()

        if data_frame.empty:
            return selected_cols

        if input.plot_types() == "Line Plot":
            req(input.line_x_axis(), input.line_y_axis())
            x_col: str = input.line_x_axis()
            y_col: str = input.line_y_axis()
            if x_col in data_frame.columns and y_col in data_frame.columns:
                selected_cols = data_frame[[x_col, y_col]]

        elif input.plot_types() == "Bar Plot":
            req(input.bar_x_axis())
            x_col: str = input.bar_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[x_col]]

        elif input.plot_types() == "Box Plot":
            req(input.box_y_axis())
            y_col: str = input.box_y_axis()
            if y_col in data_frame.columns:
                selected_cols = data_frame[[y_col]]
        
        elif input.plot_types() == "Grouped_Box Plot":
            req(input.grouped_box_y_axis(), input.grouped_box_grouping())
            y_col: str = input.grouped_box_y_axis()
            grouping_col: str = input.grouped_box_grouping()
            if y_col in data_frame.columns and grouping_col in data_frame.columns:
                selected_cols = data_frame[[y_col, grouping_col]]

        elif input.plot_types() == "Histogram":
            req(input.histogram_x_axis())
            x_col: str = input.histogram_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[x_col]]

        elif input.plot_types() == "Scatter Plot":
            req(input.scatter_x_axis(), input.scatter_y_axis())
            x_col: str = input.scatter_x_axis()
            y_col: str = input.scatter_y_axis()
            if x_col in data_frame.columns and y_col in data_frame.columns:
                selected_cols = data_frame[[x_col, y_col]]

        return selected_cols

    # Step 5: Generate Plots
    @render.plot
    @reactive.event(input.generate)
    def get_output_plot():
        print("The generate plot button is clicked.")
        data_frame = reactive_df.get()
        color_by_choices = reactive_df.get().columns.tolist()

        # ui.update_select(
        #     id="color_by",
        #     label="Color by",
        #     choices=color_by_choices
        # ),

        # Line Plot:
        if input.plot_types() == "Line Plot":
            req(input.line_x_axis(), input.line_y_axis(), input.line_plot_title())
            plot_title = input.line_plot_title()
            x_axis_title=input.line_x_axis_title()
            y_axis_title=input.line_y_axis_title()
            markers = input.markers()

            sns.set_theme()
            plt.figure(figsize=(10, 6))
            line_plot = sns.lineplot(
                data = data_frame,
                x = input.line_x_axis(),
                y = input.line_y_axis(),
                markers = markers,
                )
            plt.title(plot_title)
            plt.xlabel(x_axis_title)
            plt.ylabel(y_axis_title)
            # plt.show()
            return_plot = line_plot
        
        # Bar Plot:        
        if input.plot_types() == "Bar Plot":
            req(input.bar_x_axis())
            plot_title = input.bar_plot_title()
            x_axis = input.bar_x_axis()
            x_axis_title = input.bar_x_axis_title()
            y_axis_title = input.bar_y_axis_title()

            sns.set_theme()
            plt.figure(figsize=(10, 6))

            bar_plot = sns.countplot(
                data = data_frame,
                x = x_axis,
                )
            plt.title(plot_title)
            plt.xlabel(x_axis_title)
            plt.ylabel(y_axis_title)
            # plt.show()
            return_plot = bar_plot

        # Box Plot:
        if input.plot_types() == "Box Plot":
            req(input.box_y_axis())
            y_axis = input.box_y_axis()
            plot_title = input.box_plot_title()
            y_axis_title = input.box_y_axis_title()

            sns.set_theme()
            plt.figure(figsize=(10, 6))
            box_plot = sns.boxplot(
                y = data_frame[y_axis],
                )
            plt.title(plot_title)
            plt.ylabel(y_axis_title)
            # plt.show()
            return_plot = box_plot
        
        # # Grouped_Box Plot:
        # if input.plot_types() == "Grouped_Box Plot":
        #     req(input.grouped_box_y_axis(), input.grouped_box_grouping())
        #     plot_title = input.grouped_box_plot_title()
        #     y_axis_title = input.grouped_box_y_axis_title()
        #     grouping = input.grouped_box_grouping()

        #     box_plot_grouped = px.box(
        #         data_frame = data_frame,
        #         x = grouping,
        #         y = input.grouped_box_y_axis(),
        #         color = grouping,
        #     ).update_layout(
        #         template="seaborn",
        #         title={"text": plot_title, "x": 0.5},
        #     ).update_yaxes(
        #         title_text = y_axis_title,
        #     )
        #     return_plot = box_plot_grouped

        # # Histogram:
        # if input.plot_types() == "Histogram":
        #     req(input.histogram_x_axis())
        #     plot_title = input.histogram_plot_title()

        #     # x_axis title
        #     x_axis_title = input.histogram_x_axis_title()
        #     y_axis_title = input.histogram_y_axis_title()

        #     histogram = px.histogram(
        #         data_frame = data_frame,
        #         x = input.histogram_x_axis(),
        #         nbins = input.histogram_bin_size(),
        #     ).update_layout(
        #         template="seaborn",
        #         title={"text": plot_title, "x": 0.5},
        #     ).update_xaxes(
        #         title_text = x_axis_title,
        #     ).update_yaxes(
        #         title_text = y_axis_title,
        #     )
        #     return_plot = histogram

        # Scatter Plot:
        if input.plot_types() == "Scatter Plot":
            req(input.scatter_x_axis(), input.scatter_y_axis())
            x_axis = input.scatter_x_axis()
            y_axis = input.scatter_y_axis()
            plot_title = input.scatter_plot_title()
            x_axis_title = input.scatter_x_axis_title()
            y_axis_title = input.scatter_y_axis_title()

            sns.set_theme()
            plt.figure(figsize=(10, 6))
            scatter_plot = sns.scatterplot(
                data = data_frame,
                x = x_axis,
                y = y_axis,
                )
            plt.title(plot_title)
            plt.xlabel(x_axis_title)
            plt.ylabel(y_axis_title)
            # plt.show()
            return_plot = scatter_plot

        decoded_image.set(functions.decode_plot(return_plot))
        print(decoded_image.get())
        return return_plot
    
    # Step 6: Chatbot
    @render.text
    @reactive.event(input.ask)

    def get_chatbot_output():
        # read the file where it saves api key
        config = configparser.ConfigParser()
        config.read('../VizAble/VizAble/credentials.ini')

        try:
            API_KEY = config['gemini_api']['SHINY_APP_API_KEY']
        except KeyError as e:
            print("Error:", e)
            return "Error reading API key"
        
        # configure the API key
        genai.configure(
            api_key = API_KEY
        )

        # initialize the model
        model = genai.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat(history = [])
        question = input.chatbot_input()

        # Send the encoded image to Gemini for analysis
        prompt="Could you please provide a summary of this plot?"

        # generate content
        if question is None:
            response = model.generate_content([decoded_image.get(), prompt])
        else:
            response = model.generate_content([decoded_image.get(), question])

        # Construct the HTML string for the ARIA live region
        # Use aria-live="assertive" to announce updates immediately
        live_region_html = ui.tags.div(response.text, style="position: absolute; left: -9999px;", aria_live="assertive")

        # Return the HTML string containing the ARIA live region
        # return ui.HTML(live_region_html)
        return live_region_html

app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
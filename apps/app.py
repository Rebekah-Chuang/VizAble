from apps import functions, introductions, upload_file, check_datatypes, select_plottypes, select_columns, generate_plots
import pandas as pd
import shinyswatch
from htmltools import css
from shiny import App, Inputs, Outputs, Session, reactive, render, ui, req, module
from shiny.types import FileInfo
from typing import Optional

app_ui = ui.page_navbar(
    # theme for the app,
    shinyswatch.theme.darkly(),

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

    title="Accessible Data Visualization",
    lang="en",
)


def server(input: Inputs, output: Outputs, session: Session):
    reactive_df: reactive.Value[pd.DataFrame] = reactive.Value(pd.DataFrame())
    reactive_dtypes_df: reactive.Value[pd.DataFrame] = reactive.Value(pd.DataFrame())

    # Step 1: Upload a File
    @reactive.Effect
    def get_reactive_df() -> None:
        """ Read the uploaded file and store it in a reactive value.
        """

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
                data_frame = pd.read_csv(
                    file[0]["datapath"],
                    sep=sep,
                    quotechar=quotechar,
                    header=0
                )
                reactive_df.set(data_frame.reset_index().fillna("N/A"))

            elif file_id == "tsv_file":
                data_frame = pd.read_table(
                    file[0]["datapath"],
                    sep="\t",
                    quotechar=quotechar,
                    header=0
                )
                reactive_df.set(data_frame.reset_index().fillna("N/A"))

            else:
                sheet_names: list[str] = functions.get_excel_sheet_names(file[0]["datapath"])
                ui.update_select(
                    id="sheet_name",
                    choices=["Select an option"] + sheet_names,
                    selected=sheet_names[0] if sheet_names else None,
                )

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
                    print(f"Error reading Excel file sheet: {e}")
                    reactive_df.set(pd.DataFrame())

    @render.data_frame
    def get_output_df() -> render.DataGrid:
        """ Render the data frame in a data grid based on the uploaded file.

        :return: A data grid to display the uploaded data frame.
        :rtype: render.DataGrid
        """
        data_frame: pd.DataFrame = reactive_df.get()
        return render.DataGrid(data_frame, row_selection_mode="multiple")
    
    @reactive.Effect
    @reactive.event(input.reset)
    def reset_selections() -> None:
        """ Reset users' selections(`file_format`, `sheet_name`), and uploaded file when the reset button is clicked.
        """
        ui.update_selectize(
            id="file_format",
            selected="Select an option",
        )
        ui.update_selectize(
            id="sheet_name",
            selected="Select an option",
        )
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
    @reactive.event(input.file_format, input.sheet_name)
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
    def update_column_to_convert_selectize() -> None:
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
    def update_convert_dtype_selectize() -> None:
        """ Update the dropdown for users to select the data type to convert to based on the uploaded data frame.
        """
        choices: list[str] = ["Select an option", "str", "int", "float"]
        ui.update_select(
            id="convert_dtype",
            choices=choices,
            selected=None
        )

    @render.data_frame
    @reactive.event(input.file_format, input.sheet_name, input.convert)
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
    def update_plot_types_selectize() -> None:
        """ Update the dropdown for users to select the plot types based on the uploaded data frame.
        """
        data_frame = reactive_df.get()
        if data_frame is not None and not data_frame.empty:
            choices: list[str] = ["Select an option", "Line Plot", "Bar Plot", "Box Plot", "Histogram", "Scatter Plot"]
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
                ),
            )

        elif input.plot_types() == "Bar Plot":
            return (
                ui.markdown(
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
                ),
            )

        elif input.plot_types() == "Box Plot":
            return (
                ui.markdown(
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
                ),
            )

        elif input.plot_types() == "Histogram":
            return (
                ui.markdown(
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
                ),
            )

        elif input.plot_types() == "Scatter Plot":
            return (
                ui.markdown(
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
                ),
            )

        else:
            return ui.markdown(
                """
                Please select a plot type.
                """
            )

    @reactive.Effect
    def update_axis_selectize() -> None:
        """ Updates dropdown options for selecting the x-axis and optionally the y-axis, based on the uploaded data and the chosen plot type.
        """
        data_frame = reactive_df.get()
        choices: list[str] = functions.return_choices_for_columns(data_frame, input.plot_types())

        # update both x-axis and y-axis dropdowns
        if input.plot_types() in ["Line Plot", "Scatter Plot"]:
            functions.update_xaxis_dropdown(input.plot_types(), choices)
            functions.update_yaxis_dropdown(input.plot_types(), choices)

        # update only x-axis dropdowns
        elif input.plot_types() in ["Bar Plot", "Box Plot", "Histogram"]:
            functions.update_xaxis_dropdown(input.plot_types(), choices)

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
            req(input.box_x_axis())
            x_col: str = input.box_x_axis()
            if x_col in data_frame.columns:
                selected_cols = data_frame[[x_col]]

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


app = App(app_ui, server)

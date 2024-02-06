## [2023-02-06]
### Chores
 - Use poetry package for better package maintenance. (#47)

## [2023-02-05]
### Fixed
 - Added level-one headings to the page.
 - Added lang attribute to the html tag to specify the language of the document.

## [2023-02-02]
### Added
 - Rescricted column choices based on the plot type selected. (#33, #34)
    - Bar Plot: Only cateogorical columns are allowed.
    - Box Plot: Only numerical columns are allowed.
    - Histogram: Only numerical columns are allowed.
    - Scatter Plot: Only numerical columns are allowed.

### Fixed
 - Fixed the problem where an error occurs when a user uploads a file but haven't selected a plot type. (#28)
 - Refactored all `ui.input_select()` to `ui.input_selectize()` to improve accessibility.

## [2024-02-01]
### Added
 - Added a dropdown to display all available sheet names if an excel file is uploaded. (#27)

### Fixed
 - Fixed a bug where the original datatypes df automatically updates during data type conversion. (#30)
 - Fixed a bug where plot types dropdown not resetting when users upload a new file. (#31)

## [2024-01-31]
### Added
 - Added error handling for unsuccessful column conversion. (#26)

## [2024-01-30]
### Fixed
 - Fixed a bug that the dataframe is not updated when users convert datatype for columns (#24)

### Changed
 - Inserted a step between uploading a file and selecting plot types for users to check and convert data types of columns. (#22)
    - Step1: Upload a file
    - Step2: Check and convert data types
    - Step3: Select plot types
    - Step4: Select columns
    - Step5: Generate plots

### Added
 - Rendered a dataframe for datatypes of columns after users upload their file. (#22)
   *Example:*

   |Column Name|Data Type|
   |-|-|
   |First Name|<class 'str'>|
   |...|...|

## [2024-01-29]
### Added
 - Added a dropdown for users to select columns after choosing a plot type.(#21)

## [2024-01-25]
### Added
 - Added introductions for different plot types based on user selection.(#12)

## [2024-01-24]
### Added
 - Added a dropdown to allow different plot types(`line plot`/`bar plot`/`box plot`/`histogram`/`scatter plot`) to be selected. (#8)
 - Added navigation tabs for different steps of the process.(#7)
    - Step1: Upload a file
    - Step2: Select plot types
    - Step3: Select columns
    - Step4: Generate plots

## [2024-01-23]
### Added
 - Added a dropdown to allow different file formats(`.csv`/`.tsv`/`.xlsx`) to be uploaded. (#4)

## [2024-01-17]
### Added
- Added a feature to the application that allows users to upload CSV files.(70ef048)
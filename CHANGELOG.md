# CHANGELOG

## Unreleased

*No description*

### Feature

- general:
  - update app title and window title ([5fff538](https://github.com/Rebekah-Chuang/VizAble/commit/5fff5388a6f5e698409058f08cb6f04f6a60e6a6)) ([#139](https://github.com/Rebekah-Chuang/VizAble/pull/139))
  - add `main()` function to `app.py` for command-line app execution ([741af59](https://github.com/Rebekah-Chuang/VizAble/commit/741af59f7bcda3c1fa49c4f1d96318125650d596)) ([#121](https://github.com/Rebekah-Chuang/VizAble/pull/121))
  - add an input action button: `reset` to erase `output_df`, and users' selection on `file_format`and `sheet_name` ([f6eacf0](https://github.com/Rebekah-Chuang/VizAble/commit/f6eacf09a0a42a70f820e13695ba185dc6c247a5)) ([#83](https://github.com/Rebekah-Chuang/VizAble/pull/83))
  - Restrict column choices based on different plot types ([1e25fcb](https://github.com/Rebekah-Chuang/VizAble/commit/1e25fcb06ad503e7a78046e52ad56c8e56e312c3)) ([#35](https://github.com/Rebekah-Chuang/VizAble/pull/35))
  - Add a dropdown to display all available sheet names if an excel file is uploaded ([86be965](https://github.com/Rebekah-Chuang/VizAble/commit/86be9656475c004fcc3fbc43bc75d46d23299bf9)) ([#27](https://github.com/Rebekah-Chuang/VizAble/pull/27))
  - Add error handling for unsuccessful column conversion ([f0e9743](https://github.com/Rebekah-Chuang/VizAble/commit/f0e974317db7c1b7b9aa7fd47a3a846d75c0e501)) ([#26](https://github.com/Rebekah-Chuang/VizAble/pull/26))
  - Added introductions for different plot types based on user selection
Fixes #9 ([56e5c27](https://github.com/Rebekah-Chuang/VizAble/commit/56e5c273f886e84b3d9e1129cc4b975967646082)) ([#12](https://github.com/Rebekah-Chuang/VizAble/pull/12))

- accessibility:
  - add `ui.tooltip` to every `ui.input_action_button` to improve accessibility ([ba75954](https://github.com/Rebekah-Chuang/VizAble/commit/ba75954658317eb4eaa08e1b393fe80130643d2d)) ([#93](https://github.com/Rebekah-Chuang/VizAble/pull/93))

### Bug Fixes

- general:
  - add exception handling to catch all errors when reading TSV and Excel files ([33b3ae4](https://github.com/Rebekah-Chuang/VizAble/commit/33b3ae443e0b97202e27726bba2ac135c87b0286)) ([#133](https://github.com/Rebekah-Chuang/VizAble/pull/133))
  - change exception handling for `read_csv_file()` to catch all errors ([0a30283](https://github.com/Rebekah-Chuang/VizAble/commit/0a302834ae9615d3ce4e6a884ab9ac66e9b55ab5)) ([#131](https://github.com/Rebekah-Chuang/VizAble/pull/131))
  - implement error handling for `ParserError` to prevent the application from crashing ([ba46241](https://github.com/Rebekah-Chuang/VizAble/commit/ba46241c508a8195e8ee14bd1729322ffb3d29e2)) ([#125](https://github.com/Rebekah-Chuang/VizAble/pull/125))
  - modify code to address `ImportError` ([e768ddd](https://github.com/Rebekah-Chuang/VizAble/commit/e768ddd02e1576adf9734bc0dfda07f0e0bd4a34)) ([#123](https://github.com/Rebekah-Chuang/VizAble/pull/123))
  - change `mock_update_select` to `mock_input_select` ([8674de9](https://github.com/Rebekah-Chuang/VizAble/commit/8674de910eed1e7bd0c5e56dca328b575e491f27)) ([#106](https://github.com/Rebekah-Chuang/VizAble/pull/106))
  - change `mock_update_select` to `mock_input_select` ([e9e4252](https://github.com/Rebekah-Chuang/VizAble/commit/e9e4252fcd5ee5f026b02ee89627bd484134c9f7)) ([#105](https://github.com/Rebekah-Chuang/VizAble/pull/105))
  - increase the width of the datatypes DataFrame so that the text within the DataFrame does not wrap ([2d948ec](https://github.com/Rebekah-Chuang/VizAble/commit/2d948ecc47a83cf517ea211334d171470aee514a)) ([#85](https://github.com/Rebekah-Chuang/VizAble/pull/85))
  - address the issue where it's not possible for `ui.input_select`and `ui.input_radio_buttons` with no items selected ([3c67a61](https://github.com/Rebekah-Chuang/VizAble/commit/3c67a617e14cb98e642bfee89bc0bca25263fb9b)) ([#78](https://github.com/Rebekah-Chuang/VizAble/pull/78))
  - specify `apps` as parent package when importing `functions` ([235a419](https://github.com/Rebekah-Chuang/VizAble/commit/235a41951d39a436ad9e933781d40d3bb1243b1a)) ([#74](https://github.com/Rebekah-Chuang/VizAble/pull/74))
  - Fixed the problem where an error occurs when a user uploads a file but hasn't selected a plot type. ([7a6dcb4](https://github.com/Rebekah-Chuang/VizAble/commit/7a6dcb45361a67fa0f969a2b2560606d915991b3)) ([#35](https://github.com/Rebekah-Chuang/VizAble/pull/35))
  - Fixed the problem where the plot types dropdown didn't return to the default when the dataframe was updated. ([48b9546](https://github.com/Rebekah-Chuang/VizAble/commit/48b9546d0cc3f4bc59be2e8343c1df35478fb02f)) ([#32](https://github.com/Rebekah-Chuang/VizAble/pull/32))
  - Fixed the issue where the original data type of a DataFrame automatically updates during data type conversion ([107dd0e](https://github.com/Rebekah-Chuang/VizAble/commit/107dd0e703e51db7bd387b699a89a6f725210a24)) ([#30](https://github.com/Rebekah-Chuang/VizAble/pull/30))
  - Update dataframe if a column's data type is changed ([3765ce5](https://github.com/Rebekah-Chuang/VizAble/commit/3765ce5bbd1d4b329703dddab617993554028246)) ([#24](https://github.com/Rebekah-Chuang/VizAble/pull/24))

- accessibility:
  - address the issue where the pop-up messages were not accessible ([210dbc2](https://github.com/Rebekah-Chuang/VizAble/commit/210dbc27b67d5fa071b942f1e543b4f12d55548f)) ([#79](https://github.com/Rebekah-Chuang/VizAble/pull/79))
  - add header landmark for panel title on each page ([e79baa7](https://github.com/Rebekah-Chuang/VizAble/commit/e79baa79e9176dbb99c0fab9a6d1a422839cde77)) ([#61](https://github.com/Rebekah-Chuang/VizAble/pull/61))
  - add one main landmark for each tab ([bbb5fe8](https://github.com/Rebekah-Chuang/VizAble/commit/bbb5fe83e954d1f6541e930795c5abea5ca0d940)) ([#59](https://github.com/Rebekah-Chuang/VizAble/pull/59))
  - the page does not contain a level-one heading ([6ed6d7c](https://github.com/Rebekah-Chuang/VizAble/commit/6ed6d7c07c22d30c6f85da6b6ca41a774f4728e2)) ([#40](https://github.com/Rebekah-Chuang/VizAble/pull/40))
  - the <html> element does not have a lang attribute ([f2dc9cd](https://github.com/Rebekah-Chuang/VizAble/commit/f2dc9cd2b78cf2c0f87556deb2729fcc880d0424)) ([#38](https://github.com/Rebekah-Chuang/VizAble/pull/38))

### Documentation

- general:
  - add `LICENSE` ([6955ecb](https://github.com/Rebekah-Chuang/VizAble/commit/6955ecb01903b175cfc30537d2c8a20f9eebcab6)) ([#141](https://github.com/Rebekah-Chuang/VizAble/pull/141))
  - update`README.md` with installation, upgrade, and running instructions ([465086c](https://github.com/Rebekah-Chuang/VizAble/commit/465086c071da8ca88d6bbc0317545dab1c0cc251)) ([#129](https://github.com/Rebekah-Chuang/VizAble/pull/129))
  - update `README.md` ([80339c3](https://github.com/Rebekah-Chuang/VizAble/commit/80339c3c71758cd843d19135ca2f92683585e948))
  - update package information in `pyproject.toml` ([7f5250e](https://github.com/Rebekah-Chuang/VizAble/commit/7f5250ef00b9593510c1b47abdfe076c2c0f60bf)) ([#123](https://github.com/Rebekah-Chuang/VizAble/pull/123))
  - update `CHANGELOG.md` ([89e3170](https://github.com/Rebekah-Chuang/VizAble/commit/89e31705240e19670848f88e0c22e1ca0d67ebd6)) ([#121](https://github.com/Rebekah-Chuang/VizAble/pull/121))
  - update `CHANGELOG.md` ([4503627](https://github.com/Rebekah-Chuang/VizAble/commit/450362732dc9959795d08a5e638547f19f774936)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - update `sphinx` documentation ([76e49c6](https://github.com/Rebekah-Chuang/VizAble/commit/76e49c69c70d96ee6c16da2edfe2774609896d69)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - update `CHANGELOG.md` ([3981ff9](https://github.com/Rebekah-Chuang/VizAble/commit/3981ff9917cfb4add95b008d4add6fd30ae84e58)) ([#117](https://github.com/Rebekah-Chuang/VizAble/pull/117))
  - update `CHANGELOG.md` ([65c7981](https://github.com/Rebekah-Chuang/VizAble/commit/65c7981446324776ee453dd8acd5bba4c237da40)) ([#115](https://github.com/Rebekah-Chuang/VizAble/pull/115))
  - update `CHANGELOG.md` ([08df49a](https://github.com/Rebekah-Chuang/VizAble/commit/08df49aa5b22ec4c19f7c97b948311b1dc6bdcc3)) ([#113](https://github.com/Rebekah-Chuang/VizAble/pull/113))
  - update `poetry.lock` and python version ([1445e3a](https://github.com/Rebekah-Chuang/VizAble/commit/1445e3ad1ed4e5239682271028e051a36f395da5)) ([#113](https://github.com/Rebekah-Chuang/VizAble/pull/113))
  - modify python version in `pyproject.toml` ([abd472e](https://github.com/Rebekah-Chuang/VizAble/commit/abd472e5d3c1b4e2c66e9a581426bcd6556ce887)) ([#113](https://github.com/Rebekah-Chuang/VizAble/pull/113))
  - update `poetry.lock` file ([437a0f6](https://github.com/Rebekah-Chuang/VizAble/commit/437a0f693f45ff8b2549a853a36f354ab57ba989)) ([#113](https://github.com/Rebekah-Chuang/VizAble/pull/113))
  - update `CHANGELOG.md` ([b823435](https://github.com/Rebekah-Chuang/VizAble/commit/b823435703dcb554faaf8b7d714532b08ef6cb06))
  - update `CHANGELOG.md` ([9f269f5](https://github.com/Rebekah-Chuang/VizAble/commit/9f269f5a17b0fff1cace53bfd74f884a1d0c657d)) ([#106](https://github.com/Rebekah-Chuang/VizAble/pull/106))
  - update `CHANGELOG.md` ([b05a349](https://github.com/Rebekah-Chuang/VizAble/commit/b05a34990b5d2056f54bf248df581e88b0d3a1c8)) ([#105](https://github.com/Rebekah-Chuang/VizAble/pull/105))
  - update `CHANGELOG.md` ([dcf5eb6](https://github.com/Rebekah-Chuang/VizAble/commit/dcf5eb64cc31fe103133f456912dd53976662fab)) ([#108](https://github.com/Rebekah-Chuang/VizAble/pull/108))
  - update `CHANGELOG.md` ([d86518d](https://github.com/Rebekah-Chuang/VizAble/commit/d86518d36857a1ba32170e4d70cf13f6208f8fb3)) ([#102](https://github.com/Rebekah-Chuang/VizAble/pull/102))
  - update `CHANGELOG.md` ([c4ed590](https://github.com/Rebekah-Chuang/VizAble/commit/c4ed590e4fcd805970b37f5052cdfae614988b94)) ([#100](https://github.com/Rebekah-Chuang/VizAble/pull/100))
  - update `sphinx` documention to include `test_update_xaxis_input_select()` function ([151957f](https://github.com/Rebekah-Chuang/VizAble/commit/151957f6ae99bfc1fc28cc94ffe92d8e58e5321e)) ([#100](https://github.com/Rebekah-Chuang/VizAble/pull/100))
  - update `CHANGELOG.md` ([1d2b8c6](https://github.com/Rebekah-Chuang/VizAble/commit/1d2b8c686cc5a75226489d4c2d3b46cb5aa62324)) ([#98](https://github.com/Rebekah-Chuang/VizAble/pull/98))
  - update `sphinx` documentation and rename function names ([51f72ed](https://github.com/Rebekah-Chuang/VizAble/commit/51f72ede71ce1662173aec0d4f290d1b7fee9a92)) ([#98](https://github.com/Rebekah-Chuang/VizAble/pull/98))
  - update `CHANGELOG.md` ([1baf586](https://github.com/Rebekah-Chuang/VizAble/commit/1baf586e63edef5ee1bfd837a2639760d4f04177)) ([#96](https://github.com/Rebekah-Chuang/VizAble/pull/96))
  - update `sphinx` documentation ([356624c](https://github.com/Rebekah-Chuang/VizAble/commit/356624cddee54d6aa7a6e64f2eed57081f809d02)) ([#96](https://github.com/Rebekah-Chuang/VizAble/pull/96))
  - add docstrings for all functions in the `app.py/server()` ([5f0bbc5](https://github.com/Rebekah-Chuang/VizAble/commit/5f0bbc560c79b675e19e1f1e8861f2d9df229652)) ([#91](https://github.com/Rebekah-Chuang/VizAble/pull/91))
  - update `CHANGELOG.md` ([7feb94a](https://github.com/Rebekah-Chuang/VizAble/commit/7feb94a6b345220c20f8eb6742583f1ba515901a)) ([#85](https://github.com/Rebekah-Chuang/VizAble/pull/85))
  - update `CHANGELOG.md` ([a62d670](https://github.com/Rebekah-Chuang/VizAble/commit/a62d6701aff1d5174854e63ce6c2ce2dd533bfd8)) ([#83](https://github.com/Rebekah-Chuang/VizAble/pull/83))
  - update `CHANGELOG.md` ([e9c6881](https://github.com/Rebekah-Chuang/VizAble/commit/e9c68818712f99b6206e09b70cbd378214e55125))
  - correctly import `functions.py` from `apps` so documentation can be successfully generated by `Sphinx` ([4b7ad8d](https://github.com/Rebekah-Chuang/VizAble/commit/4b7ad8da0adebd2d75404a72faa31d083103edbe)) ([#72](https://github.com/Rebekah-Chuang/VizAble/pull/72))
  - switch from Google docstring format to Sphinx docstring format ([2c6fa73](https://github.com/Rebekah-Chuang/VizAble/commit/2c6fa73db85ad1be038e03beda0d5b5b7a809e6b)) ([#70](https://github.com/Rebekah-Chuang/VizAble/pull/70))
  - modify the docstring in functions.py by using the autoDocstring - Python Docstring Generator extension ([1b4900a](https://github.com/Rebekah-Chuang/VizAble/commit/1b4900ab47b891e64fa2b0cb19fd373b7c8908dc)) ([#70](https://github.com/Rebekah-Chuang/VizAble/pull/70))
  - add type annotations for functions in `app.py/server()` ([675510c](https://github.com/Rebekah-Chuang/VizAble/commit/675510c15af2dfe5d4dd8076c64ae8e629bfbc52)) ([#66](https://github.com/Rebekah-Chuang/VizAble/pull/66))
  - add type annotation for functions in `functions.py` ([03b0853](https://github.com/Rebekah-Chuang/VizAble/commit/03b0853d34f3364a70fd619b9175118b62ce49e0)) ([#63](https://github.com/Rebekah-Chuang/VizAble/pull/63))
  - update `CHANGELOG.md` ([159d4d8](https://github.com/Rebekah-Chuang/VizAble/commit/159d4d84ee09dea85057a092a5667604a164b247)) ([#47](https://github.com/Rebekah-Chuang/VizAble/pull/47))
  - add `accessibility` to `conventionalCommits.scopes` ([cfab43f](https://github.com/Rebekah-Chuang/VizAble/commit/cfab43f323e96acac5260ff860f8f848d007944e))
  - update `CHANGELOG.md` ([a2ddf78](https://github.com/Rebekah-Chuang/VizAble/commit/a2ddf78fcf608255ad452e3567f013d70ce3e815)) ([#40](https://github.com/Rebekah-Chuang/VizAble/pull/40))
  - update `CHANGELOG.md` ([d061972](https://github.com/Rebekah-Chuang/VizAble/commit/d0619722c15eb71c5746ad4460f9bb96742b6663)) ([#35](https://github.com/Rebekah-Chuang/VizAble/pull/35))
  - Update `CHANGELOG.md` ([3892dd2](https://github.com/Rebekah-Chuang/VizAble/commit/3892dd21cfb97bae964cdb5769778a62f3543644)) ([#32](https://github.com/Rebekah-Chuang/VizAble/pull/32))
  - update `CHANGELOG.md` ([73c69ce](https://github.com/Rebekah-Chuang/VizAble/commit/73c69cee8a24ca08b01ccee94633bf2c0d758bd8))
  - Update `CHANGELOG.md` ([9d10eba](https://github.com/Rebekah-Chuang/VizAble/commit/9d10eba297290972a710f8f3dc78301c64752d6d)) ([#24](https://github.com/Rebekah-Chuang/VizAble/pull/24))

### Refactor

- general:
  - move read csv logic to `functions.py` in order to test ([f797228](https://github.com/Rebekah-Chuang/VizAble/commit/f797228bbc134fb253460f4d9fb8ca0a03ba1c9c)) ([#127](https://github.com/Rebekah-Chuang/VizAble/pull/127))
  - remove unused import ([de97266](https://github.com/Rebekah-Chuang/VizAble/commit/de9726664774a856aaf596eae00e76f4020c6263)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - import module correctly for testing ([f0b33ff](https://github.com/Rebekah-Chuang/VizAble/commit/f0b33ffdf967cfca1926538d068111839c3f14bc)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - change directory name `apps` to `VizAble` ([86c47a5](https://github.com/Rebekah-Chuang/VizAble/commit/86c47a5d2d7913b93302d570b2f7a836cdf6ff8a)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - improve `return_choices_for_columns()` function to enhance readability ([ac0f9bf](https://github.com/Rebekah-Chuang/VizAble/commit/ac0f9bf815baa0b4f540dc66a97d6646b36b16d6)) ([#110](https://github.com/Rebekah-Chuang/VizAble/pull/110))
  - move update x-axis/y-axis input_select based on different plot types to `functions.py` for enhanced modularity ([d6a46af](https://github.com/Rebekah-Chuang/VizAble/commit/d6a46af0b9c8f04b8a3eb098b6434643ec4cf5e5)) ([#98](https://github.com/Rebekah-Chuang/VizAble/pull/98))
  - refactor column choices logic based on different plot types for enhanced modularity ([0c23ef8](https://github.com/Rebekah-Chuang/VizAble/commit/0c23ef8c047c5089f88086ae44202fe243904192)) ([#96](https://github.com/Rebekah-Chuang/VizAble/pull/96))
  - separate `app.py` into different modules ([2b1aac6](https://github.com/Rebekah-Chuang/VizAble/commit/2b1aac68d485ed3f93469fbe79eec334fcc7a9f0)) ([#94](https://github.com/Rebekah-Chuang/VizAble/pull/94))
  - remove `@output` decorator from the app since it's no longer needed ([112319f](https://github.com/Rebekah-Chuang/VizAble/commit/112319f1c031cf9429fbb6abf6fe3bb61bde8a15)) ([#88](https://github.com/Rebekah-Chuang/VizAble/pull/88))
  - change `update_selectize` to `update_select` ([f312992](https://github.com/Rebekah-Chuang/VizAble/commit/f31299288bdbdb14612db82e0c02bbc014c6ddad)) ([#82](https://github.com/Rebekah-Chuang/VizAble/pull/82))
  - remove empty folder ([8454437](https://github.com/Rebekah-Chuang/VizAble/commit/845443734681450103298c4ac2fca318183dde38))
  - move `test_dataframe` folder to `tests` folder for better organization ([47906b6](https://github.com/Rebekah-Chuang/VizAble/commit/47906b686645d937a77c6c99c7dcb7522a694648)) ([#54](https://github.com/Rebekah-Chuang/VizAble/pull/54))
  - move `get_excel_sheet_names()` into `functions.py` for better unit testing ([6f1e05e](https://github.com/Rebekah-Chuang/VizAble/commit/6f1e05e990b05701728b8e228ddc0da8342dee85)) ([#52](https://github.com/Rebekah-Chuang/VizAble/pull/52))
  - change `ui.input_selectize` to `ui.input_select` to improve accessibility ([f68fd13](https://github.com/Rebekah-Chuang/VizAble/commit/f68fd13c0b02a9c7767585cdd0358a8823025e51))

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*

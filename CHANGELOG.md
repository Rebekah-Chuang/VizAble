# CHANGELOG

## Unreleased

*No description*

### Feature

- general:
  - update app title and window title ([5fff538](https://github.com/Rebekah-Chuang/VizAble/commit/5fff5388a6f5e698409058f08cb6f04f6a60e6a6)) ([#139](https://github.com/Rebekah-Chuang/VizAble/pull/139))
  - add `main()` function to `app.py` for command-line app execution ([741af59](https://github.com/Rebekah-Chuang/VizAble/commit/741af59f7bcda3c1fa49c4f1d96318125650d596)) ([#121](https://github.com/Rebekah-Chuang/VizAble/pull/121))
  - add an input action button: `reset` to erase `output_df`, and users' selection on `file_format`and `sheet_name` ([f6eacf0](https://github.com/Rebekah-Chuang/VizAble/commit/f6eacf09a0a42a70f820e13695ba185dc6c247a5)) ([#83](https://github.com/Rebekah-Chuang/VizAble/pull/83))
  - restrict column choices based on different plot types ([1e25fcb](https://github.com/Rebekah-Chuang/VizAble/commit/1e25fcb06ad503e7a78046e52ad56c8e56e312c3)) ([#35](https://github.com/Rebekah-Chuang/VizAble/pull/35))
  - add a dropdown to display all available sheet names if an excel file is uploaded ([86be965](https://github.com/Rebekah-Chuang/VizAble/commit/86be9656475c004fcc3fbc43bc75d46d23299bf9)) ([#27](https://github.com/Rebekah-Chuang/VizAble/pull/27))
  - add error handling for unsuccessful column conversion ([f0e9743](https://github.com/Rebekah-Chuang/VizAble/commit/f0e974317db7c1b7b9aa7fd47a3a846d75c0e501)) ([#26](https://github.com/Rebekah-Chuang/VizAble/pull/26))
  - add introductions for different plot types based on user selection
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
  - fix the problem where an error occurs when a user uploads a file but hasn't selected a plot type. ([7a6dcb4](https://github.com/Rebekah-Chuang/VizAble/commit/7a6dcb45361a67fa0f969a2b2560606d915991b3)) ([#35](https://github.com/Rebekah-Chuang/VizAble/pull/35))
  - fix the problem where the plot types dropdown didn't return to the default when the dataframe was updated. ([48b9546](https://github.com/Rebekah-Chuang/VizAble/commit/48b9546d0cc3f4bc59be2e8343c1df35478fb02f)) ([#32](https://github.com/Rebekah-Chuang/VizAble/pull/32))
  - fix the issue where the original data type of a DataFrame automatically updates during data type conversion ([107dd0e](https://github.com/Rebekah-Chuang/VizAble/commit/107dd0e703e51db7bd387b699a89a6f725210a24)) ([#30](https://github.com/Rebekah-Chuang/VizAble/pull/30))
  - update dataframe if a column's data type is changed ([3765ce5](https://github.com/Rebekah-Chuang/VizAble/commit/3765ce5bbd1d4b329703dddab617993554028246)) ([#24](https://github.com/Rebekah-Chuang/VizAble/pull/24))

- accessibility:
  - address the issue where the pop-up messages were not accessible ([210dbc2](https://github.com/Rebekah-Chuang/VizAble/commit/210dbc27b67d5fa071b942f1e543b4f12d55548f)) ([#79](https://github.com/Rebekah-Chuang/VizAble/pull/79))
  - add header landmark for panel title on each page ([e79baa7](https://github.com/Rebekah-Chuang/VizAble/commit/e79baa79e9176dbb99c0fab9a6d1a422839cde77)) ([#61](https://github.com/Rebekah-Chuang/VizAble/pull/61))
  - add one main landmark for each tab ([bbb5fe8](https://github.com/Rebekah-Chuang/VizAble/commit/bbb5fe83e954d1f6541e930795c5abea5ca0d940)) ([#59](https://github.com/Rebekah-Chuang/VizAble/pull/59))
  - the page does not contain a level-one heading ([6ed6d7c](https://github.com/Rebekah-Chuang/VizAble/commit/6ed6d7c07c22d30c6f85da6b6ca41a774f4728e2)) ([#40](https://github.com/Rebekah-Chuang/VizAble/pull/40))
  - the <html> element does not have a lang attribute ([f2dc9cd](https://github.com/Rebekah-Chuang/VizAble/commit/f2dc9cd2b78cf2c0f87556deb2729fcc880d0424)) ([#38](https://github.com/Rebekah-Chuang/VizAble/pull/38))

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

###  Chores

- general:
  - add chore to `CHANGELOG.md` ([394bbec](https://github.com/Rebekah-Chuang/VizAble/commit/394bbec625c3a6eef3751813e5155b1a688013f9))
  - add `changelog.yaml` workflow ([ca28faf](https://github.com/Rebekah-Chuang/VizAble/commit/ca28fafade91f49bbb5127f388800c43f9e1e10d))
  - update `shiny` version to 0.8.0 ([c85c362](https://github.com/Rebekah-Chuang/VizAble/commit/c85c3620615e31714c9ce6401ae88e990932466c)) ([#137](https://github.com/Rebekah-Chuang/VizAble/pull/137))
  - remove `.DS_Store` files from the repository ([452b5c4](https://github.com/Rebekah-Chuang/VizAble/commit/452b5c4c46f9de7e1f6a1b0a4c5bb013e7510b3a)) ([#125](https://github.com/Rebekah-Chuang/VizAble/pull/125))
  - add `dist/` to `.gitignore` ([a52fc02](https://github.com/Rebekah-Chuang/VizAble/commit/a52fc0278b898e342a6d05424fc89eba7ea06e1a)) ([#123](https://github.com/Rebekah-Chuang/VizAble/pull/123))
  - add `.DS_Store` to `.gitignore` ([65a1b37](https://github.com/Rebekah-Chuang/VizAble/commit/65a1b37507dc1245f7d9a1f92f6fe3e73be1ad03)) ([#119](https://github.com/Rebekah-Chuang/VizAble/pull/119))
  - add `.gitignore` ([209426d](https://github.com/Rebekah-Chuang/VizAble/commit/209426d128cfc3adb76b1a968b81429441ee8937)) ([#117](https://github.com/Rebekah-Chuang/VizAble/pull/117))
  - add `tox` workflow to run tests ([047a204](https://github.com/Rebekah-Chuang/VizAble/commit/047a204d401274c104c784d4f9c2c3ce3659c7b7)) ([#113](https://github.com/Rebekah-Chuang/VizAble/pull/113))
  - update `pytest.yaml` ([f8a1249](https://github.com/Rebekah-Chuang/VizAble/commit/f8a1249d3c195801481aea01e5eaf7263bad352d))
  - trigger github actions when push to main branch ([cb1d270](https://github.com/Rebekah-Chuang/VizAble/commit/cb1d2702ceb1c4d4e806c43bf2247d599dcc63cf))
  - install `sphinx-press-theme` using `poetry` ([ea520eb](https://github.com/Rebekah-Chuang/VizAble/commit/ea520ebf78d6e0060006772dff7620b9e0531452)) ([#72](https://github.com/Rebekah-Chuang/VizAble/pull/72))
  - generate documentation using `sphinx` by executing `make html` ([de6b53a](https://github.com/Rebekah-Chuang/VizAble/commit/de6b53a7bda71f86b8f8bbe4d19b19455f475532)) ([#72](https://github.com/Rebekah-Chuang/VizAble/pull/72))
  - setup for sphinx before executing `make html` ([734a2e3](https://github.com/Rebekah-Chuang/VizAble/commit/734a2e3afd2f5a9e7a60952395eca36193bf0624)) ([#72](https://github.com/Rebekah-Chuang/VizAble/pull/72))
  - install `sphinx` using `poetry` ([1fb5591](https://github.com/Rebekah-Chuang/VizAble/commit/1fb55916d4d0bc40df59c5cf42f231f377ca5c7f)) ([#72](https://github.com/Rebekah-Chuang/VizAble/pull/72))
  - modify `pytest.yaml` and only keep `python-version: ["3.12"]` ([c651ffb](https://github.com/Rebekah-Chuang/VizAble/commit/c651ffbcf15c3a5818789412d5dfa5de56326028)) ([#68](https://github.com/Rebekah-Chuang/VizAble/pull/68))
  - add Github actions set up `.github/workflows/pytest.yaml` ([5356946](https://github.com/Rebekah-Chuang/VizAble/commit/53569468aef69b709dc6ed7edcdf141ee49c9506)) ([#68](https://github.com/Rebekah-Chuang/VizAble/pull/68))
  - use poetry package for better package maintenance
closes #45 ([5e9572e](https://github.com/Rebekah-Chuang/VizAble/commit/5e9572ea450b2149dfcbaaa2c2ddf63e0fb84ee4)) ([#47](https://github.com/Rebekah-Chuang/VizAble/pull/47))

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*

# CHANGELOG



## v0.5.4 (2024-03-07)

### Ci

* ci: trigger publish to PyPI workflow when releasing [skip ci] ([`560cc30`](https://github.com/Rebekah-Chuang/VizAble/commit/560cc3072da9ff6c1cfda63a8fdfe120b823e866))

### Fix

* fix: modify instructions in home page [skip ci] ([`6a57f60`](https://github.com/Rebekah-Chuang/VizAble/commit/6a57f60636db1754b61cfd8db2cd2b1d0eec4b59))


## v0.5.3 (2024-03-07)

### Chore

* chore: use python 3.10 for semantic release workflow ([`b160e8c`](https://github.com/Rebekah-Chuang/VizAble/commit/b160e8c3c6421b7ed677e8c16ac872fe20068744))

### Ci

* ci: modify `semantic-release` add `pypi-publish` workflow [skip ci] ([`7e2b629`](https://github.com/Rebekah-Chuang/VizAble/commit/7e2b62978294690461124cf9d4a3d8a59978ff0d))

### Fix

* fix: modify instructions in the home page [skip ci] ([`6d7e6f3`](https://github.com/Rebekah-Chuang/VizAble/commit/6d7e6f309593d26219f49ca13df851dfd9e38cfa))


## v0.5.2 (2024-03-08)

### Build

* build(deps): bump starlette from 0.34.0 to 0.36.2

  Bumps [starlette](https://github.com/encode/starlette) from 0.34.0 to 0.36.2.
  - [Release notes](https://github.com/encode/starlette/releases)
  - [Changelog](https://github.com/encode/starlette/blob/master/docs/release-notes.md)
  - [Commits](https://github.com/encode/starlette/compare/0.34.0...0.36.2)

  updated-dependencies:
  - dependency-name: starlette
  - dependency-type: indirect
  ...

  Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fef0a15`](https://github.com/Rebekah-Chuang/VizAble/commit/fef0a15315c82519e770700ae05786b9f829b022))

### Chore

* chore: manually update version to 0.5.2 to align with pypi published version ([`564f103`](https://github.com/Rebekah-Chuang/VizAble/commit/564f10304ff37ff156defa2e17b5e3f0949d7610))

* chore: add `python-semantic-release` ([`4367590`](https://github.com/Rebekah-Chuang/VizAble/commit/4367590bade61f76b8c98222a2c8beb2868df529))

* chore: update `shiny` version to 0.8.0 ([`c85c362`](https://github.com/Rebekah-Chuang/VizAble/commit/c85c3620615e31714c9ce6401ae88e990932466c))

* chore: remove `.DS_Store` files from the repository ([`452b5c4`](https://github.com/Rebekah-Chuang/VizAble/commit/452b5c4c46f9de7e1f6a1b0a4c5bb013e7510b3a))

* chore: add `dist/` to `.gitignore` ([`a52fc02`](https://github.com/Rebekah-Chuang/VizAble/commit/a52fc0278b898e342a6d05424fc89eba7ea06e1a))

* chore: add `.DS_Store` to `.gitignore` ([`65a1b37`](https://github.com/Rebekah-Chuang/VizAble/commit/65a1b37507dc1245f7d9a1f92f6fe3e73be1ad03))

* chore: add `.gitignore` ([`209426d`](https://github.com/Rebekah-Chuang/VizAble/commit/209426d128cfc3adb76b1a968b81429441ee8937))

* chore: add `tox` workflow to run tests ([`047a204`](https://github.com/Rebekah-Chuang/VizAble/commit/047a204d401274c104c784d4f9c2c3ce3659c7b7))

* chore: install `sphinx-press-theme` using `poetry` ([`ea520eb`](https://github.com/Rebekah-Chuang/VizAble/commit/ea520ebf78d6e0060006772dff7620b9e0531452))

* chore: generate documentation using `sphinx` by executing `make html` ([`de6b53a`](https://github.com/Rebekah-Chuang/VizAble/commit/de6b53a7bda71f86b8f8bbe4d19b19455f475532))

* chore: prepare setup for `sphinx` before executing `make html` ([`734a2e3`](https://github.com/Rebekah-Chuang/VizAble/commit/734a2e3afd2f5a9e7a60952395eca36193bf0624))

* chore: install `sphinx` using `poetry` ([`1fb5591`](https://github.com/Rebekah-Chuang/VizAble/commit/1fb55916d4d0bc40df59c5cf42f231f377ca5c7f))
* chore: use `poetry` package for better package maintenance
closes #45 ([`5e9572e`](https://github.com/Rebekah-Chuang/VizAble/commit/5e9572ea450b2149dfcbaaa2c2ddf63e0fb84ee4))

* chore: add `accessibility` to `conventionalCommits.scopes` ([`cfab43f`](https://github.com/Rebekah-Chuang/VizAble/commit/cfab43f323e96acac5260ff860f8f848d007944e))

### Ci

* ci: add `python-semantic-release.yaml` workflow ([`dacef43`](https://github.com/Rebekah-Chuang/VizAble/commit/dacef4393615a008cfea443997e2d138eef3502f))

* ci: add `lint-commit-message.yaml` to github action workflows (#143) ([`0619f8e`](https://github.com/Rebekah-Chuang/VizAble/commit/0619f8e0e72c83b84831093c180627341310d685))

* ci: modify `tox.yaml` to run on ubuntu-latest ([`3f2c1dc`](https://github.com/Rebekah-Chuang/VizAble/commit/3f2c1dc9cd13cd4843306f34208b839f6bf605a1))

### Documentation
* docs: add `LICENSE` ([`6955ecb`](https://github.com/Rebekah-Chuang/VizAble/commit/6955ecb01903b175cfc30537d2c8a20f9eebcab6))

* docs: update`README.md` with installation, upgrade, and running instructions ([`465086c`](https://github.com/Rebekah-Chuang/VizAble/commit/465086c071da8ca88d6bbc0317545dab1c0cc251))

* docs: update package information in `pyproject.toml` ([`7f5250e`](https://github.com/Rebekah-Chuang/VizAble/commit/7f5250ef00b9593510c1b47abdfe076c2c0f60bf))

* docs: update `sphinx` documentation ([`76e49c6`](https://github.com/Rebekah-Chuang/VizAble/commit/76e49c69c70d96ee6c16da2edfe2774609896d69))

* docs: update `poetry.lock` and python version ([`1445e3a`](https://github.com/Rebekah-Chuang/VizAble/commit/1445e3ad1ed4e5239682271028e051a36f395da5))

* docs: modify python version in `pyproject.toml` ([`abd472e`](https://github.com/Rebekah-Chuang/VizAble/commit/abd472e5d3c1b4e2c66e9a581426bcd6556ce887))

* docs: update `poetry.lock` file ([`437a0f6`](https://github.com/Rebekah-Chuang/VizAble/commit/437a0f693f45ff8b2549a853a36f354ab57ba989))

* docs: update `sphinx` documention to include `test_update_xaxis_input_select()` function ([`151957f`](https://github.com/Rebekah-Chuang/VizAble/commit/151957f6ae99bfc1fc28cc94ffe92d8e58e5321e))

* docs: update `sphinx` documentation and rename function names ([`51f72ed`](https://github.com/Rebekah-Chuang/VizAble/commit/51f72ede71ce1662173aec0d4f290d1b7fee9a92))

* docs: update `sphinx` documentation ([`356624c`](https://github.com/Rebekah-Chuang/VizAble/commit/356624cddee54d6aa7a6e64f2eed57081f809d02))

* docs: add docstrings for all functions in the `app.py/server()` ([`5f0bbc5`](https://github.com/Rebekah-Chuang/VizAble/commit/5f0bbc560c79b675e19e1f1e8861f2d9df229652))

* docs: import `functions.py` from `apps` correctly so documentation can be successfully generated by `Sphinx` ([`4b7ad8d`](https://github.com/Rebekah-Chuang/VizAble/commit/4b7ad8da0adebd2d75404a72faa31d083103edbe))

* docs: switch from Google docstring format to `Sphinx` docstring format ([`2c6fa73`](https://github.com/Rebekah-Chuang/VizAble/commit/2c6fa73db85ad1be038e03beda0d5b5b7a809e6b))

* docs: modify the docstring in `functions.py` by using the **autoDocstring - Python Docstring Generator extension** ([`1b4900a`](https://github.com/Rebekah-Chuang/VizAble/commit/1b4900ab47b891e64fa2b0cb19fd373b7c8908dc))

* docs: add type annotations for functions in `app.py/server()` ([`675510c`](https://github.com/Rebekah-Chuang/VizAble/commit/675510c15af2dfe5d4dd8076c64ae8e629bfbc52))

* docs: add type annotation for functions in `functions.py` ([`03b0853`](https://github.com/Rebekah-Chuang/VizAble/commit/03b0853d34f3364a70fd619b9175118b62ce49e0))

### Feature

* feat: update app title and window title ([`5fff538`](https://github.com/Rebekah-Chuang/VizAble/commit/5fff5388a6f5e698409058f08cb6f04f6a60e6a6))

* feat: add `main()` function to `app.py` for command-line app execution ([`741af59`](https://github.com/Rebekah-Chuang/VizAble/commit/741af59f7bcda3c1fa49c4f1d96318125650d596))

* feat(accessibility): add `ui.tooltip` to every `ui.input_action_button` to improve accessibility ([`ba75954`](https://github.com/Rebekah-Chuang/VizAble/commit/ba75954658317eb4eaa08e1b393fe80130643d2d))

* feat: add an input action button: `reset` to erase `output_df`, and users&#39; selection on `file_format`and `sheet_name` ([`f6eacf0`](https://github.com/Rebekah-Chuang/VizAble/commit/f6eacf09a0a42a70f820e13695ba185dc6c247a5))

* feat: restrict column choices based on different plot types ([`1e25fcb`](https://github.com/Rebekah-Chuang/VizAble/commit/1e25fcb06ad503e7a78046e52ad56c8e56e312c3))

* feat: add a dropdown to display all available sheet names if an excel file is uploaded ([`86be965`](https://github.com/Rebekah-Chuang/VizAble/commit/86be9656475c004fcc3fbc43bc75d46d23299bf9))

* feat: add error handling for unsuccessful column conversion ([`f0e9743`](https://github.com/Rebekah-Chuang/VizAble/commit/f0e974317db7c1b7b9aa7fd47a3a846d75c0e501))

* feat: add introductions for different plot types based on user selection
Fixes #9 ([`56e5c27`](https://github.com/Rebekah-Chuang/VizAble/commit/56e5c273f886e84b3d9e1129cc4b975967646082))

* feat: display datatypes to user when uploading files ([`28ce413`](https://github.com/Rebekah-Chuang/VizAble/commit/28ce41356244727bdc30512b3293ad4971a294d7))

* feat: add dropdowns for users to select columns(x-axis/y-axis)
Fixes #13 ([`7715193`](https://github.com/Rebekah-Chuang/VizAble/commit/7715193397b2277873e9e774ddc476b38cec0d9c))

* feat: add a dropdown for users to select different plot types
Fixes #8 ([`bbf12d9`](https://github.com/Rebekah-Chuang/VizAble/commit/bbf12d99d34232a90d927380f8e726acc41d3732))

* feat: add navigation tabs/pages for different steps of the process
Fixes #5 ([`d0b6dbe`](https://github.com/Rebekah-Chuang/VizAble/commit/d0b6dbe72c22b6e3e8d9973dc1c1983ec33196d5))

* feat: add a dropdown to allow different file formats (.csv, .tsv, .xlsx).
Fixes #3 ([`86d6136`](https://github.com/Rebekah-Chuang/VizAble/commit/86d6136725a18f370f07e533d93aa15e9e9c38ba))

* feat: add `ui.input_file()` for users to upload file ([`70ef048`](https://github.com/Rebekah-Chuang/VizAble/commit/70ef048d4839caeaaaddd6812fda1d6c68880c4f))

### Fix

* fix: add exception handling to catch all errors when reading TSV and Excel files ([`33b3ae4`](https://github.com/Rebekah-Chuang/VizAble/commit/33b3ae443e0b97202e27726bba2ac135c87b0286))

* fix: change exception handling for `read_csv_file()` to catch all errors ([`0a30283`](https://github.com/Rebekah-Chuang/VizAble/commit/0a302834ae9615d3ce4e6a884ab9ac66e9b55ab5))

* fix: implement error handling for `ParserError` to prevent the application from crashing ([`ba46241`](https://github.com/Rebekah-Chuang/VizAble/commit/ba46241c508a8195e8ee14bd1729322ffb3d29e2))

* fix: modify code to address `ImportError` ([`e768ddd`](https://github.com/Rebekah-Chuang/VizAble/commit/e768ddd02e1576adf9734bc0dfda07f0e0bd4a34))

* fix: change `mock_update_select` to `mock_input_select` ([`8674de9`](https://github.com/Rebekah-Chuang/VizAble/commit/8674de910eed1e7bd0c5e56dca328b575e491f27))

* fix: change `mock_update_select` to `mock_input_select` ([`e9e4252`](https://github.com/Rebekah-Chuang/VizAble/commit/e9e4252fcd5ee5f026b02ee89627bd484134c9f7))

* fix: increase the width of the datatypes DataFrame so that the text within the DataFrame does not wrap ([`2d948ec`](https://github.com/Rebekah-Chuang/VizAble/commit/2d948ecc47a83cf517ea211334d171470aee514a))

* fix(accessibility): address the issue where the pop-up messages were not accessible ([`210dbc2`](https://github.com/Rebekah-Chuang/VizAble/commit/210dbc27b67d5fa071b942f1e543b4f12d55548f))

* fix: address the issue where it&#39;s not possible for `ui.input_select`and `ui.input_radio_buttons` with no items selected ([`3c67a61`](https://github.com/Rebekah-Chuang/VizAble/commit/3c67a617e14cb98e642bfee89bc0bca25263fb9b))

* fix: specify `apps` as parent package when importing `functions` ([`235a419`](https://github.com/Rebekah-Chuang/VizAble/commit/235a41951d39a436ad9e933781d40d3bb1243b1a))

* fix(accessibility): add header landmark for panel title on each page ([`e79baa7`](https://github.com/Rebekah-Chuang/VizAble/commit/e79baa79e9176dbb99c0fab9a6d1a422839cde77))

* fix(accessibility): add one main landmark for each tab ([`bbb5fe8`](https://github.com/Rebekah-Chuang/VizAble/commit/bbb5fe83e954d1f6541e930795c5abea5ca0d940))

* fix(accessibility): address the issue where the page does not contain a level-one heading ([`6ed6d7c`](https://github.com/Rebekah-Chuang/VizAble/commit/6ed6d7c07c22d30c6f85da6b6ca41a774f4728e2))

* fix(accessibility): the &lt;html&gt; element does not have a lang attribute ([`f2dc9cd`](https://github.com/Rebekah-Chuang/VizAble/commit/f2dc9cd2b78cf2c0f87556deb2729fcc880d0424))

* fix: an error occurs when a user uploads a file but hasn&#39;t selected a plot type ([`7a6dcb4`](https://github.com/Rebekah-Chuang/VizAble/commit/7a6dcb45361a67fa0f969a2b2560606d915991b3))

* fix: address the problem where the plot types dropdown didn&#39;t return to the default when the dataframe was updated. ([`48b9546`](https://github.com/Rebekah-Chuang/VizAble/commit/48b9546d0cc3f4bc59be2e8343c1df35478fb02f))

* fix: address the issue where the original data type of a DataFrame automatically updates during data type conversion ([`107dd0e`](https://github.com/Rebekah-Chuang/VizAble/commit/107dd0e703e51db7bd387b699a89a6f725210a24))

* fix: update dataframe if a column&#39;s data type is changed ([`3765ce5`](https://github.com/Rebekah-Chuang/VizAble/commit/3765ce5bbd1d4b329703dddab617993554028246))

### Refactor

* refactor: move read csv logic to `functions.py` in order to test ([`f797228`](https://github.com/Rebekah-Chuang/VizAble/commit/f797228bbc134fb253460f4d9fb8ca0a03ba1c9c))

* refactor: remove unused import ([`de97266`](https://github.com/Rebekah-Chuang/VizAble/commit/de9726664774a856aaf596eae00e76f4020c6263))

* refactor: import module correctly for testing ([`f0b33ff`](https://github.com/Rebekah-Chuang/VizAble/commit/f0b33ffdf967cfca1926538d068111839c3f14bc))

* refactor: change directory name `apps` to `VizAble` ([`86c47a5`](https://github.com/Rebekah-Chuang/VizAble/commit/86c47a5d2d7913b93302d570b2f7a836cdf6ff8a))

* refactor: improve `return_choices_for_columns()` function to enhance readability ([`ac0f9bf`](https://github.com/Rebekah-Chuang/VizAble/commit/ac0f9bf815baa0b4f540dc66a97d6646b36b16d6))

* refactor: move update x-axis/y-axis input_select based on different plot types to `functions.py` for enhanced modularity ([`d6a46af`](https://github.com/Rebekah-Chuang/VizAble/commit/d6a46af0b9c8f04b8a3eb098b6434643ec4cf5e5))

* refactor: refactor column choices logic based on different plot types for enhanced modularity ([`0c23ef8`](https://github.com/Rebekah-Chuang/VizAble/commit/0c23ef8c047c5089f88086ae44202fe243904192))

* refactor: separate `app.py` into different modules ([`2b1aac6`](https://github.com/Rebekah-Chuang/VizAble/commit/2b1aac68d485ed3f93469fbe79eec334fcc7a9f0))

* refactor: remove `@output` decorator from the app since it&#39;s no longer needed ([`112319f`](https://github.com/Rebekah-Chuang/VizAble/commit/112319f1c031cf9429fbb6abf6fe3bb61bde8a15))

* refactor: change `update_selectize` to `update_select` ([`f312992`](https://github.com/Rebekah-Chuang/VizAble/commit/f31299288bdbdb14612db82e0c02bbc014c6ddad))

* refactor: remove empty folder ([`8454437`](https://github.com/Rebekah-Chuang/VizAble/commit/845443734681450103298c4ac2fca318183dde38))

* refactor: move `test_dataframe` folder to `tests` folder for better organization ([`47906b6`](https://github.com/Rebekah-Chuang/VizAble/commit/47906b686645d937a77c6c99c7dcb7522a694648))

* refactor: move `get_excel_sheet_names()` into `functions.py` for better unit testing ([`6f1e05e`](https://github.com/Rebekah-Chuang/VizAble/commit/6f1e05e990b05701728b8e228ddc0da8342dee85))

* refactor: change `ui.input_selectize` to `ui.input_select` to improve accessibility ([`f68fd13`](https://github.com/Rebekah-Chuang/VizAble/commit/f68fd13c0b02a9c7767585cdd0358a8823025e51))

### Style

* style(theme): modify app theme to `cosmo` ([`494f259`](https://github.com/Rebekah-Chuang/VizAble/commit/494f259f2a8bdf7a285847605ef317e7ff3b3e21))

### Test

* test: fix test failure in `test_read_csv_file_invalid()` by adjusting expected output ([`8bc6d52`](https://github.com/Rebekah-Chuang/VizAble/commit/8bc6d52f869582bb516e6417bad190b67eb324bd))

* test: add unit test for `read_csv_file()` function to test both valid and invalid file ([`a05a873`](https://github.com/Rebekah-Chuang/VizAble/commit/a05a8735ce471162baae8952e23e57a0e305995e))

* test: reduce test dataframe to only 5 rows to test edge case ([`3d399ae`](https://github.com/Rebekah-Chuang/VizAble/commit/3d399ae306eda8d45be3c5adb33eeb0b436178be))

* test: add 2 csv files to test `ParserError` ([`51ae798`](https://github.com/Rebekah-Chuang/VizAble/commit/51ae798753b8b1c612202961d2a8ce26dd212b52))

* test: add unit test for `input_file()` function ([`6250806`](https://github.com/Rebekah-Chuang/VizAble/commit/625080684aee8d8a693ddff0c29882b207cdf6f7))

* test: add unit test for `yaxis_input_select()` function ([`7bb4f32`](https://github.com/Rebekah-Chuang/VizAble/commit/7bb4f3217a957c92fcfe0c68a76cd8303f0c28ef))

* test: add unit test for `xaxis_input_select()` function ([`524afb7`](https://github.com/Rebekah-Chuang/VizAble/commit/524afb71bb47ac89ee55c98100e891a0bb640ede))

* test: add unit test for `update_yaxis_input_select()` function ([`f505dff`](https://github.com/Rebekah-Chuang/VizAble/commit/f505dff7ec41d8362522942d1ae3a1313f72f227))

* test: add unit test for `update_xaxis_input_select()` function ([`9bb463f`](https://github.com/Rebekah-Chuang/VizAble/commit/9bb463f882cb57d1fa7b6188d6d9ba16eb3d8aa8))

* test: add unit test for `return_choices_for_columns()` function ([`45aea21`](https://github.com/Rebekah-Chuang/VizAble/commit/45aea21e561eff11b79763ff54f1e5d23746dc1a))

* test: add unit test for `functions.py/get_excel_sheet_names()` ([`4fa02dd`](https://github.com/Rebekah-Chuang/VizAble/commit/4fa02dd250f6213fcccc3a22ef483cfd1a7ace6a))

* test: update `test_get_file_id()` in `tests/test_functions.py` ([`d4327f3`](https://github.com/Rebekah-Chuang/VizAble/commit/d4327f3716b3b947d7067de4b6c5d972e3bf1c3d))

* test: add comment for `test_get_file_id ` ([`1d83b67`](https://github.com/Rebekah-Chuang/VizAble/commit/1d83b67adeea5035972b4f54091a98c5c3291cfb))

* test: add unit test for `functions.py/get_file_id()` ([`c7ec250`](https://github.com/Rebekah-Chuang/VizAble/commit/c7ec250cb5f5f0e4add9841f6291cc18e99b57c6))

* test: generate test dataframe ([`a0b50a0`](https://github.com/Rebekah-Chuang/VizAble/commit/a0b50a0723611c2340bdfc6c4cdc231f898f88a9))
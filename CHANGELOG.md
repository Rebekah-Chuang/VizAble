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

* ci: add `-vv` to `semantic-release -vv publish` [skip ci] ([`5308ce8`](https://github.com/Rebekah-Chuang/VizAble/commit/5308ce8c391906f9e8a82c555cf22c6330c0d55a))

* ci: remove `commit_author=&#34;github-actions &lt;action@github.com&gt;&#34;` after `semantic-release publish` ([`7356b4a`](https://github.com/Rebekah-Chuang/VizAble/commit/7356b4a0a33ca9862e7e8bcbc0ec7ecfd9775884))

* ci: remove `-D` in semantic-release command [skip ci] ([`17c97fd`](https://github.com/Rebekah-Chuang/VizAble/commit/17c97fdbb29a2a9ea01fb2ea92f1473965f096e3))

* ci: add double quote around python version (&#34;3.10&#34;) in semantic release workflow [skip ci] ([`d777d03`](https://github.com/Rebekah-Chuang/VizAble/commit/d777d03110fbfa849ff0253ee89a90acd41d02d6))

### Fix

* fix: modify instructions in the home page [skip ci] ([`6d7e6f3`](https://github.com/Rebekah-Chuang/VizAble/commit/6d7e6f309593d26219f49ca13df851dfd9e38cfa))


## v0.5.2 (2024-03-08)

### Build

* build(deps): bump starlette from 0.34.0 to 0.36.2

Bumps [starlette](https://github.com/encode/starlette) from 0.34.0 to 0.36.2.
- [Release notes](https://github.com/encode/starlette/releases)
- [Changelog](https://github.com/encode/starlette/blob/master/docs/release-notes.md)
- [Commits](https://github.com/encode/starlette/compare/0.34.0...0.36.2)

---
updated-dependencies:
- dependency-name: starlette
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fef0a15`](https://github.com/Rebekah-Chuang/VizAble/commit/fef0a15315c82519e770700ae05786b9f829b022))

* build: upgrate to version 0.5.1 and add poetry scripts ([`972bc09`](https://github.com/Rebekah-Chuang/VizAble/commit/972bc0983ac86642d145b7fe03f280523883f582))

### Chore

* chore: manually update version to 0.5.2 to align with pypi published version ([`564f103`](https://github.com/Rebekah-Chuang/VizAble/commit/564f10304ff37ff156defa2e17b5e3f0949d7610))

* chore: add `python-semantic-release` ([`4367590`](https://github.com/Rebekah-Chuang/VizAble/commit/4367590bade61f76b8c98222a2c8beb2868df529))

* chore: add chore to `CHANGELOG.md` ([`394bbec`](https://github.com/Rebekah-Chuang/VizAble/commit/394bbec625c3a6eef3751813e5155b1a688013f9))

* chore: add `changelog.yaml` workflow ([`ca28faf`](https://github.com/Rebekah-Chuang/VizAble/commit/ca28fafade91f49bbb5127f388800c43f9e1e10d))

* chore: update `shiny` version to 0.8.0 ([`c85c362`](https://github.com/Rebekah-Chuang/VizAble/commit/c85c3620615e31714c9ce6401ae88e990932466c))

* chore: remove `.DS_Store` files from the repository ([`452b5c4`](https://github.com/Rebekah-Chuang/VizAble/commit/452b5c4c46f9de7e1f6a1b0a4c5bb013e7510b3a))

* chore: add `dist/` to `.gitignore` ([`a52fc02`](https://github.com/Rebekah-Chuang/VizAble/commit/a52fc0278b898e342a6d05424fc89eba7ea06e1a))

* chore: add `.DS_Store` to `.gitignore` ([`65a1b37`](https://github.com/Rebekah-Chuang/VizAble/commit/65a1b37507dc1245f7d9a1f92f6fe3e73be1ad03))

* chore: add `.gitignore` ([`209426d`](https://github.com/Rebekah-Chuang/VizAble/commit/209426d128cfc3adb76b1a968b81429441ee8937))

* chore: add `tox` workflow to run tests ([`047a204`](https://github.com/Rebekah-Chuang/VizAble/commit/047a204d401274c104c784d4f9c2c3ce3659c7b7))

* chore: update `pytest.yaml` ([`f8a1249`](https://github.com/Rebekah-Chuang/VizAble/commit/f8a1249d3c195801481aea01e5eaf7263bad352d))

* chore: trigger github actions when push to main branch ([`cb1d270`](https://github.com/Rebekah-Chuang/VizAble/commit/cb1d2702ceb1c4d4e806c43bf2247d599dcc63cf))

* chore: install `sphinx-press-theme` using `poetry` ([`ea520eb`](https://github.com/Rebekah-Chuang/VizAble/commit/ea520ebf78d6e0060006772dff7620b9e0531452))

* chore: generate documentation using `sphinx` by executing `make html` ([`de6b53a`](https://github.com/Rebekah-Chuang/VizAble/commit/de6b53a7bda71f86b8f8bbe4d19b19455f475532))

* chore: setup for sphinx before executing `make html` ([`734a2e3`](https://github.com/Rebekah-Chuang/VizAble/commit/734a2e3afd2f5a9e7a60952395eca36193bf0624))

* chore: install `sphinx` using `poetry` ([`1fb5591`](https://github.com/Rebekah-Chuang/VizAble/commit/1fb55916d4d0bc40df59c5cf42f231f377ca5c7f))

* chore: modify `pytest.yaml` and only keep `python-version: [&#34;3.12&#34;]` ([`c651ffb`](https://github.com/Rebekah-Chuang/VizAble/commit/c651ffbcf15c3a5818789412d5dfa5de56326028))

* chore: add Github actions set up `.github/workflows/pytest.yaml` ([`5356946`](https://github.com/Rebekah-Chuang/VizAble/commit/53569468aef69b709dc6ed7edcdf141ee49c9506))

* chore: use poetry package for better package maintenance
closes #45 ([`5e9572e`](https://github.com/Rebekah-Chuang/VizAble/commit/5e9572ea450b2149dfcbaaa2c2ddf63e0fb84ee4))

### Ci

* ci: update `python-semantic-release.yaml` [skip ci] ([`d7e5b7e`](https://github.com/Rebekah-Chuang/VizAble/commit/d7e5b7e98afe0e5476aacd378e89ffa2e99ce4b8))

* ci: add `python-semantic-release.yaml` workflow ([`dacef43`](https://github.com/Rebekah-Chuang/VizAble/commit/dacef4393615a008cfea443997e2d138eef3502f))

* ci: add `lint-commit-message.yaml` to github action workflows (#143) ([`0619f8e`](https://github.com/Rebekah-Chuang/VizAble/commit/0619f8e0e72c83b84831093c180627341310d685))

* ci: modify `tox.yaml` to run on ubuntu-latest ([`3f2c1dc`](https://github.com/Rebekah-Chuang/VizAble/commit/3f2c1dc9cd13cd4843306f34208b839f6bf605a1))

* ci: remove `pytest.yaml` from github action workflows ([`1a0446d`](https://github.com/Rebekah-Chuang/VizAble/commit/1a0446df4efd911b5237d4c5ae68fecf360e5b6b))

* ci: trigger github action when pushing to main ([`98b61aa`](https://github.com/Rebekah-Chuang/VizAble/commit/98b61aad5c07cc2e5e2e4d06c1df5ba1413f3375))

### Documentation

* docs(CHANGELOG): update `CHANGELOG.md` ([`e1e42a8`](https://github.com/Rebekah-Chuang/VizAble/commit/e1e42a804940ad71f315b696f808b591834047e0))

* docs(CHANGELOG): update `CHANGELOG.md` ([`fd198cc`](https://github.com/Rebekah-Chuang/VizAble/commit/fd198cc218b53d309acc12dd5def8a01aff2bd66))

* docs(CHANGELOG): update `CHANGELOG.md` ([`0f750e9`](https://github.com/Rebekah-Chuang/VizAble/commit/0f750e992ff27360d5772fa63c3dc116094e626b))

* docs(CHANGELOG): update `CHANGELOG.md` ([`be52ce9`](https://github.com/Rebekah-Chuang/VizAble/commit/be52ce91c73944943c75a0190917021f7bd64f1a))

* docs(CHANGELOG): update `CHANGELOG.md` ([`2b99b76`](https://github.com/Rebekah-Chuang/VizAble/commit/2b99b76945ed4ed0859a2efba56da5312b29437d))

* docs: add `LICENSE` ([`6955ecb`](https://github.com/Rebekah-Chuang/VizAble/commit/6955ecb01903b175cfc30537d2c8a20f9eebcab6))

* docs: update`README.md` with installation, upgrade, and running instructions ([`465086c`](https://github.com/Rebekah-Chuang/VizAble/commit/465086c071da8ca88d6bbc0317545dab1c0cc251))

* docs: update `README.md` ([`80339c3`](https://github.com/Rebekah-Chuang/VizAble/commit/80339c3c71758cd843d19135ca2f92683585e948))

* docs: update package information in `pyproject.toml` ([`7f5250e`](https://github.com/Rebekah-Chuang/VizAble/commit/7f5250ef00b9593510c1b47abdfe076c2c0f60bf))

* docs: update `CHANGELOG.md` ([`89e3170`](https://github.com/Rebekah-Chuang/VizAble/commit/89e31705240e19670848f88e0c22e1ca0d67ebd6))

* docs: update `CHANGELOG.md` ([`4503627`](https://github.com/Rebekah-Chuang/VizAble/commit/450362732dc9959795d08a5e638547f19f774936))

* docs: update `sphinx` documentation ([`76e49c6`](https://github.com/Rebekah-Chuang/VizAble/commit/76e49c69c70d96ee6c16da2edfe2774609896d69))

* docs: update `CHANGELOG.md` ([`3981ff9`](https://github.com/Rebekah-Chuang/VizAble/commit/3981ff9917cfb4add95b008d4add6fd30ae84e58))

* docs: update `CHANGELOG.md` ([`65c7981`](https://github.com/Rebekah-Chuang/VizAble/commit/65c7981446324776ee453dd8acd5bba4c237da40))

* docs: update `CHANGELOG.md` ([`08df49a`](https://github.com/Rebekah-Chuang/VizAble/commit/08df49aa5b22ec4c19f7c97b948311b1dc6bdcc3))

* docs: update `poetry.lock` and python version ([`1445e3a`](https://github.com/Rebekah-Chuang/VizAble/commit/1445e3ad1ed4e5239682271028e051a36f395da5))

* docs: modify python version in `pyproject.toml` ([`abd472e`](https://github.com/Rebekah-Chuang/VizAble/commit/abd472e5d3c1b4e2c66e9a581426bcd6556ce887))

* docs: update `poetry.lock` file ([`437a0f6`](https://github.com/Rebekah-Chuang/VizAble/commit/437a0f693f45ff8b2549a853a36f354ab57ba989))

* docs: update `CHANGELOG.md` ([`b823435`](https://github.com/Rebekah-Chuang/VizAble/commit/b823435703dcb554faaf8b7d714532b08ef6cb06))

* docs: update `CHANGELOG.md` ([`9f269f5`](https://github.com/Rebekah-Chuang/VizAble/commit/9f269f5a17b0fff1cace53bfd74f884a1d0c657d))

* docs: update `CHANGELOG.md` ([`b05a349`](https://github.com/Rebekah-Chuang/VizAble/commit/b05a34990b5d2056f54bf248df581e88b0d3a1c8))

* docs: update `CHANGELOG.md` ([`dcf5eb6`](https://github.com/Rebekah-Chuang/VizAble/commit/dcf5eb64cc31fe103133f456912dd53976662fab))

* docs: update `CHANGELOG.md` ([`d86518d`](https://github.com/Rebekah-Chuang/VizAble/commit/d86518d36857a1ba32170e4d70cf13f6208f8fb3))

* docs: update `CHANGELOG.md` ([`c4ed590`](https://github.com/Rebekah-Chuang/VizAble/commit/c4ed590e4fcd805970b37f5052cdfae614988b94))

* docs: update `sphinx` documention to include `test_update_xaxis_input_select()` function ([`151957f`](https://github.com/Rebekah-Chuang/VizAble/commit/151957f6ae99bfc1fc28cc94ffe92d8e58e5321e))

* docs: update `CHANGELOG.md` ([`1d2b8c6`](https://github.com/Rebekah-Chuang/VizAble/commit/1d2b8c686cc5a75226489d4c2d3b46cb5aa62324))

* docs: update `sphinx` documentation and rename function names ([`51f72ed`](https://github.com/Rebekah-Chuang/VizAble/commit/51f72ede71ce1662173aec0d4f290d1b7fee9a92))

* docs: update `CHANGELOG.md` ([`1baf586`](https://github.com/Rebekah-Chuang/VizAble/commit/1baf586e63edef5ee1bfd837a2639760d4f04177))

* docs: update `sphinx` documentation ([`356624c`](https://github.com/Rebekah-Chuang/VizAble/commit/356624cddee54d6aa7a6e64f2eed57081f809d02))

* docs: add docstrings for all functions in the `app.py/server()` ([`5f0bbc5`](https://github.com/Rebekah-Chuang/VizAble/commit/5f0bbc560c79b675e19e1f1e8861f2d9df229652))

* docs: update `CHANGELOG.md` ([`7feb94a`](https://github.com/Rebekah-Chuang/VizAble/commit/7feb94a6b345220c20f8eb6742583f1ba515901a))

* docs: update `CHANGELOG.md` ([`a62d670`](https://github.com/Rebekah-Chuang/VizAble/commit/a62d6701aff1d5174854e63ce6c2ce2dd533bfd8))

* docs: update `CHANGELOG.md` ([`e9c6881`](https://github.com/Rebekah-Chuang/VizAble/commit/e9c68818712f99b6206e09b70cbd378214e55125))

* docs: correctly import `functions.py` from `apps` so documentation can be successfully generated by `Sphinx` ([`4b7ad8d`](https://github.com/Rebekah-Chuang/VizAble/commit/4b7ad8da0adebd2d75404a72faa31d083103edbe))

* docs: switch from Google docstring format to Sphinx docstring format ([`2c6fa73`](https://github.com/Rebekah-Chuang/VizAble/commit/2c6fa73db85ad1be038e03beda0d5b5b7a809e6b))

* docs: modify the docstring in functions.py by using the autoDocstring - Python Docstring Generator extension ([`1b4900a`](https://github.com/Rebekah-Chuang/VizAble/commit/1b4900ab47b891e64fa2b0cb19fd373b7c8908dc))

* docs: add type annotations for functions in `app.py/server()` ([`675510c`](https://github.com/Rebekah-Chuang/VizAble/commit/675510c15af2dfe5d4dd8076c64ae8e629bfbc52))

* docs: add type annotation for functions in `functions.py` ([`03b0853`](https://github.com/Rebekah-Chuang/VizAble/commit/03b0853d34f3364a70fd619b9175118b62ce49e0))

* docs: update `CHANGELOG.md` ([`159d4d8`](https://github.com/Rebekah-Chuang/VizAble/commit/159d4d84ee09dea85057a092a5667604a164b247))

* docs: add `accessibility` to `conventionalCommits.scopes` ([`cfab43f`](https://github.com/Rebekah-Chuang/VizAble/commit/cfab43f323e96acac5260ff860f8f848d007944e))

* docs: update `CHANGELOG.md` ([`a2ddf78`](https://github.com/Rebekah-Chuang/VizAble/commit/a2ddf78fcf608255ad452e3567f013d70ce3e815))

* docs: update `CHANGELOG.md` ([`d061972`](https://github.com/Rebekah-Chuang/VizAble/commit/d0619722c15eb71c5746ad4460f9bb96742b6663))

* docs: Update `CHANGELOG.md` ([`3892dd2`](https://github.com/Rebekah-Chuang/VizAble/commit/3892dd21cfb97bae964cdb5769778a62f3543644))

* docs: update `CHANGELOG.md` ([`73c69ce`](https://github.com/Rebekah-Chuang/VizAble/commit/73c69cee8a24ca08b01ccee94633bf2c0d758bd8))

* docs: Update `CHANGELOG.md` ([`9d10eba`](https://github.com/Rebekah-Chuang/VizAble/commit/9d10eba297290972a710f8f3dc78301c64752d6d))

### Feature

* feat: update app title and window title ([`5fff538`](https://github.com/Rebekah-Chuang/VizAble/commit/5fff5388a6f5e698409058f08cb6f04f6a60e6a6))

* feat: add `main()` function to `app.py` for command-line app execution ([`741af59`](https://github.com/Rebekah-Chuang/VizAble/commit/741af59f7bcda3c1fa49c4f1d96318125650d596))

* feat(accessibility): add `ui.tooltip` to every `ui.input_action_button` to improve accessibility ([`ba75954`](https://github.com/Rebekah-Chuang/VizAble/commit/ba75954658317eb4eaa08e1b393fe80130643d2d))

* feat: add an input action button: `reset` to erase `output_df`, and users&#39; selection on `file_format`and `sheet_name` ([`f6eacf0`](https://github.com/Rebekah-Chuang/VizAble/commit/f6eacf09a0a42a70f820e13695ba185dc6c247a5))

* feat: Restrict column choices based on different plot types ([`1e25fcb`](https://github.com/Rebekah-Chuang/VizAble/commit/1e25fcb06ad503e7a78046e52ad56c8e56e312c3))

* feat: Add a dropdown to display all available sheet names if an excel file is uploaded ([`86be965`](https://github.com/Rebekah-Chuang/VizAble/commit/86be9656475c004fcc3fbc43bc75d46d23299bf9))

* feat: Add error handling for unsuccessful column conversion ([`f0e9743`](https://github.com/Rebekah-Chuang/VizAble/commit/f0e974317db7c1b7b9aa7fd47a3a846d75c0e501))

* feat: Added introductions for different plot types based on user selection
Fixes #9 ([`56e5c27`](https://github.com/Rebekah-Chuang/VizAble/commit/56e5c273f886e84b3d9e1129cc4b975967646082))

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

* fix(accessibility): add one main landmark for each tab

Instructions, Step1, Step2, Step3 ,Step4 ([`bbb5fe8`](https://github.com/Rebekah-Chuang/VizAble/commit/bbb5fe83e954d1f6541e930795c5abea5ca0d940))

* fix(accessibility): the page does not contain a level-one heading ([`6ed6d7c`](https://github.com/Rebekah-Chuang/VizAble/commit/6ed6d7c07c22d30c6f85da6b6ca41a774f4728e2))

* fix(accessibility): the &lt;html&gt; element does not have a lang attribute ([`f2dc9cd`](https://github.com/Rebekah-Chuang/VizAble/commit/f2dc9cd2b78cf2c0f87556deb2729fcc880d0424))

* fix: Fixed the problem where an error occurs when a user uploads a file but hasn&#39;t selected a plot type. ([`7a6dcb4`](https://github.com/Rebekah-Chuang/VizAble/commit/7a6dcb45361a67fa0f969a2b2560606d915991b3))

* fix: Fixed the problem where the plot types dropdown didn&#39;t return to the default when the dataframe was updated. ([`48b9546`](https://github.com/Rebekah-Chuang/VizAble/commit/48b9546d0cc3f4bc59be2e8343c1df35478fb02f))

* fix: Fixed the issue where the original data type of a DataFrame automatically updates during data type conversion ([`107dd0e`](https://github.com/Rebekah-Chuang/VizAble/commit/107dd0e703e51db7bd387b699a89a6f725210a24))

* fix: Update dataframe if a column&#39;s data type is changed ([`3765ce5`](https://github.com/Rebekah-Chuang/VizAble/commit/3765ce5bbd1d4b329703dddab617993554028246))

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

* test: add unit test for `return_choices_for_columns()` function

This commit adds unit tests for the `return_choices_for_columns()` function to verify that it returns a list of column names with the appropriate data type when a user selects a specific plot type. For instance, a line plot should return all column names; a bar plot should return only columns with categorical data types; and box plots, histograms, and scatter plots should return only columns with numerical data types.

`@pytest.mark.parametrize is also used in this unit test to test with different plot types, thereby avoiding repetition. ([`45aea21`](https://github.com/Rebekah-Chuang/VizAble/commit/45aea21e561eff11b79763ff54f1e5d23746dc1a))

* test: add unit test for `functions.py/get_excel_sheet_names()` ([`4fa02dd`](https://github.com/Rebekah-Chuang/VizAble/commit/4fa02dd250f6213fcccc3a22ef483cfd1a7ace6a))

* test: update `test_get_file_id()` in `tests/test_functions.py` ([`d4327f3`](https://github.com/Rebekah-Chuang/VizAble/commit/d4327f3716b3b947d7067de4b6c5d972e3bf1c3d))

* test: add comment for `test_get_file_id ` ([`1d83b67`](https://github.com/Rebekah-Chuang/VizAble/commit/1d83b67adeea5035972b4f54091a98c5c3291cfb))

* test: add unit test for `functions.py/get_file_id()` ([`c7ec250`](https://github.com/Rebekah-Chuang/VizAble/commit/c7ec250cb5f5f0e4add9841f6291cc18e99b57c6))

### Unknown

* Merge pull request #149 from Rebekah-Chuang:Rebekah-Chuang/issue148

chore: implement python semantic release workflow ([`9c62a4b`](https://github.com/Rebekah-Chuang/VizAble/commit/9c62a4b5f39b70b75e8ba10018ce77f498e0cd60))

* Merge branch &#39;main&#39; of https://github.com/Rebekah-Chuang/accessible-data-viz-application ([`c9b34e2`](https://github.com/Rebekah-Chuang/VizAble/commit/c9b34e2c2f3a1867ebded7653b147d3d8eefc887))

* Merge branch &#39;main&#39; of https://github.com/Rebekah-Chuang/accessible-data-viz-application ([`05b315f`](https://github.com/Rebekah-Chuang/VizAble/commit/05b315f3da9a26b3dd0041b15adbbc532c8c7e4f))

* Merge pull request #144 from Rebekah-Chuang/dependabot/pip/starlette-0.36.2

build(deps): bump starlette from 0.34.0 to 0.36.2 ([`ade398f`](https://github.com/Rebekah-Chuang/VizAble/commit/ade398fae48c6a3dc564fc8f59c7c85e4642e2a5))

* Merge pull request #141 from Rebekah-Chuang/add-license

docs: add `LICENSE` ([`261441a`](https://github.com/Rebekah-Chuang/VizAble/commit/261441ab64863e31f6b32a73afb07abe7d0b9af2))

* Merge pull request #139 from Rebekah-Chuang:Rebekah-Chuang/issue138

feat: update app title and window title ([`18de4cc`](https://github.com/Rebekah-Chuang/VizAble/commit/18de4cc9ccd13afe15852289183718b9e8da9303))

* Merge pull request #137 from Rebekah-Chuang:Rebekah-Chuang/issue136

chore: update `shiny` version to 0.8.0 ([`8859573`](https://github.com/Rebekah-Chuang/VizAble/commit/8859573cabefc0dddc32558a2748ff034e9153cc))

* Merge pull request #135 from Rebekah-Chuang:Rebekah-Chuang/issue134

test: reduce test dataframe size and add unit test for `read_csv_file()` function ([`78ce76b`](https://github.com/Rebekah-Chuang/VizAble/commit/78ce76b2228808e4847c503853635415225064aa))

* Merge pull request #133 from Rebekah-Chuang:Rebekah-Chuang/issue132

fix: add exception handling to catch all errors when reading TSV and Excel files ([`37648dd`](https://github.com/Rebekah-Chuang/VizAble/commit/37648dd5e6bcb30901cb0dc2e7118d97df84020f))

* Merge pull request #131 from Rebekah-Chuang:Rebekah-Chuang/issue130

fix: change exception handling for `read_csv_file()` to catch all errors ([`69500bb`](https://github.com/Rebekah-Chuang/VizAble/commit/69500bb4c2b00a5a82f58a49cf05f8ca9946d830))

* Merge pull request #129 from Rebekah-Chuang:Rebekah-Chuang/issue128

docs: update `README.md` with installation, upgrade, and running instructions ([`3bd2ebb`](https://github.com/Rebekah-Chuang/VizAble/commit/3bd2ebb2a7dfe0400aa5aebd6558e15010e3239d))

* Merge pull request #127 from Rebekah-Chuang:Rebekah-Chuang/issue126

refactor: move read csv logic to `functions.py` in order to test ([`d432a0e`](https://github.com/Rebekah-Chuang/VizAble/commit/d432a0ebc11dacda4ae209c8623bda255a14ead5))

* Merge pull request #125 from Rebekah-Chuang:Rebekah-Chuang/issue124

fix: handle `ParserError` when uploading incorrect csv file ([`a6d7e5e`](https://github.com/Rebekah-Chuang/VizAble/commit/a6d7e5e461b94407292764293a0ac6a590fbe8a9))

* Merge pull request #123 from Rebekah-Chuang:Rebekah-Chuang/issue122

build: publish VizAble 0.5.1 to PyPI ([`b922de8`](https://github.com/Rebekah-Chuang/VizAble/commit/b922de885900f66873c82181923286e1c06b79f5))

* Merge pull request #121 from Rebekah-Chuang:Rebekah-Chuang/issue120

feat: add `main()` function to `app.py` for command-line app execution ([`03dff11`](https://github.com/Rebekah-Chuang/VizAble/commit/03dff11119d11477b8e93fd25599afbe3e90f3f6))

* Merge pull request #119 from Rebekah-Chuang:Rebekah-Chuang/issue118

refactor: change directory name from `apps` to `VizAble` ([`c2bb203`](https://github.com/Rebekah-Chuang/VizAble/commit/c2bb2038b0f59b195962a4e2a974443e676721f6))

* Merge pull request #117 from Rebekah-Chuang:Rebekah-Chuang/issue116

chore: add `.gitignore` ([`13cf69d`](https://github.com/Rebekah-Chuang/VizAble/commit/13cf69df3f71edae6aaae0937537f81f21a9177e))

* Merge pull request #115 from Rebekah-Chuang:Rebekah-Chuang/issue114

ci: remove `pytest.yaml` from github action workflows ([`79a8421`](https://github.com/Rebekah-Chuang/VizAble/commit/79a8421601403ee344266acef942fdb710dfb6b2))

* Merge pull request #113 from Rebekah-Chuang:Rebekah-Chuang/issue112

chore: add `tox` workflow to run tests ([`4e3b9b2`](https://github.com/Rebekah-Chuang/VizAble/commit/4e3b9b295b3bb16000d90fbaf0608a75115dd0ed))

* Merge pull request #110 from Rebekah-Chuang:Rebekah-Chuang/issue109

refactor: improve `return_choices_for_columns()` function to enhance readability ([`2c5733a`](https://github.com/Rebekah-Chuang/VizAble/commit/2c5733ad059e963aee7a8a4ade9b41b9501bab4d))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue109 ([`298648f`](https://github.com/Rebekah-Chuang/VizAble/commit/298648ff38e59ffc3140ce60c2fb19805264b009))

* Merge pull request #106 from Rebekah-Chuang:Rebekah-Chuang/issue104

test: add unit test for `yaxis_input_select()` function ([`567c50f`](https://github.com/Rebekah-Chuang/VizAble/commit/567c50f1c6b744e29623b2fec9c6590dbd247460))

* Merge branch &#39;main&#39; into Rebekah-Chuang/issue104 ([`fe11697`](https://github.com/Rebekah-Chuang/VizAble/commit/fe116977abdac712b8258f61531e78d42ced47bd))

* Merge pull request #105 from Rebekah-Chuang:Rebekah-Chuang/issue103

test: add unit test for `xaxis_input_select()` function ([`e9e0f76`](https://github.com/Rebekah-Chuang/VizAble/commit/e9e0f764b9a9e400d2827c829c28a5b9a52ca351))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue109 ([`4f9c72f`](https://github.com/Rebekah-Chuang/VizAble/commit/4f9c72f21a07dc387ac7c58a8dfba2c5ae3211ba))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue104 ([`6eeefb2`](https://github.com/Rebekah-Chuang/VizAble/commit/6eeefb2fdc03dbd53f6d5bd16b786703e6932808))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue103 ([`065bb63`](https://github.com/Rebekah-Chuang/VizAble/commit/065bb636180c3549a7ebd06ba6944c214196055b))

* Merge pull request #108 from Rebekah-Chuang:Rebekah-Chuang/issue107

test: add unit test for `input_file()` function ([`bd9c143`](https://github.com/Rebekah-Chuang/VizAble/commit/bd9c143358df00d535519a3edf5315e8002d6457))

* Merge pull request #102 from Rebekah-Chuang:Rebekah-Chuang/issue101

test: add unit test for `update_yaxis_input_select()` function ([`930af84`](https://github.com/Rebekah-Chuang/VizAble/commit/930af84c91e7d2fbf7e48b87210ffc92a718bba2))

* Merge branch &#39;main&#39; into Rebekah-Chuang/issue101 ([`0ea7fd0`](https://github.com/Rebekah-Chuang/VizAble/commit/0ea7fd07c48d715f6625c2c4e52d5c0356c10b57))

* Merge pull request #100 from Rebekah-Chuang:Rebekah-Chuang/issue99

test: add unit test for `update_xaxis_input_select()` function ([`ebe6fdc`](https://github.com/Rebekah-Chuang/VizAble/commit/ebe6fdc90ab33df2f2fcb99ba20c479ad88aa850))

* Merge pull request #98 from Rebekah-Chuang:Rebekah-Chuang/issue97

refactor: move update x-axis/y-axis input_select based on different plot types to `functions.py` for enhanced modularity ([`a5d1747`](https://github.com/Rebekah-Chuang/VizAble/commit/a5d1747dcd7c90ee5c3db262eb5562672d079c09))

* Merge pull request #96 from Rebekah-Chuang:Rebekah-Chuang/issue95

refactor: move column choices logic based on different plot types to `functions.py` for enhanced modularity ([`ee56269`](https://github.com/Rebekah-Chuang/VizAble/commit/ee5626950552d82bd918d59d5c1b887b129b2d7a))

* Merge pull request #93 from Rebekah-Chuang:Rebekah-Chuang/issue92

feat(accessibility): add `ui.tooltip` to every `ui.input_action_button` to improve accessibility ([`b4ff9dd`](https://github.com/Rebekah-Chuang/VizAble/commit/b4ff9dd7851e99c06cad715949982639d4566c7f))

* Merge branch &#39;main&#39; into Rebekah-Chuang/issue92 ([`e964038`](https://github.com/Rebekah-Chuang/VizAble/commit/e964038d4fcfcc814a4c22cc42036487a1018c39))

* Merge pull request #94 from Rebekah-Chuang:Rebekah-Chuang/issue89

refactor: separate `app.py` into different modules ([`689ec66`](https://github.com/Rebekah-Chuang/VizAble/commit/689ec66b07651cc42313a41af100f466ff1fba3d))

* Merge pull request #91 from Rebekah-Chuang:Rebekah-Chuang/issue90

docs: add docstrings for all functions in the `app.py/server()` ([`e951f46`](https://github.com/Rebekah-Chuang/VizAble/commit/e951f4697def05732831656a1feca45e99451910))

* Merge pull request #88 from Rebekah-Chuang:Rebekah-Chuang/issue87

refactor: remove `@output` decorator from the app since it&#39;s no longer needed ([`98d5510`](https://github.com/Rebekah-Chuang/VizAble/commit/98d5510b1e2ed74d26ea516207c40761f9854ac3))

* Merge pull request #85 from Rebekah-Chuang:Rebekah-Chuang/issue84

fix: increase the width of the datatypes DataFrame so that the text within the DataFrame does not wrap ([`abe9d56`](https://github.com/Rebekah-Chuang/VizAble/commit/abe9d566d1ad7ee64d312466283b2179eef7be9f))

* Merge pull request #82 from Rebekah-Chuang:Rebekah-Chuang/issue81

refactor: change `update_selectize` to `update_select` ([`0190af3`](https://github.com/Rebekah-Chuang/VizAble/commit/0190af3b3682d2c3e49a7df4a3846431dce184ae))

* Merge branch &#39;main&#39; into Rebekah-Chuang/issue81 ([`5bd8ee2`](https://github.com/Rebekah-Chuang/VizAble/commit/5bd8ee294ccbd9713f17cbb7e7813349decadb82))

* Merge pull request #83 from Rebekah-Chuang:Rebekah-Chuang/issue75

feat: add an input action button: `reset` to erase `output_df`, and users&#39; selection on `file_format`and `sheet_name` ([`25b1575`](https://github.com/Rebekah-Chuang/VizAble/commit/25b157585f26c31c32c0b243ee319f5238fc987e))

* Merge pull request #79 from Rebekah-Chuang:Rebekah-Chuang/issue77

fix(accessibility): address the issue where the pop-up messages were not accessible ([`877bf9c`](https://github.com/Rebekah-Chuang/VizAble/commit/877bf9c596b9456fd49550116bd0b68ec4df1bc1))

* Merge pull request #78 from Rebekah-Chuang:Rebekah-Chuang/issue76

fix: address the issue where it&#39;s not possible for `ui.input_select` and `ui.input_radio_buttons` with no items selected ([`0de5ba9`](https://github.com/Rebekah-Chuang/VizAble/commit/0de5ba9f7f91e1cc4bf50005e0edbfa6c88f6085))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue76 ([`1ee9c53`](https://github.com/Rebekah-Chuang/VizAble/commit/1ee9c536a87d06e98d5bda8f6ca5910840ea5db9))

* Merge pull request #74 from Rebekah-Chuang:Rebekah-Chuang/issue73

fix: specify `apps` as parent package when importing `functions` ([`2ffe27a`](https://github.com/Rebekah-Chuang/VizAble/commit/2ffe27a8e2f4d440b7c128561dcc56e72186b4ad))

* Merge pull request #72 from Rebekah-Chuang:Rebekah-Chuang/issue71

docs: auto-generate documentation using `Sphinx` ([`2c74cb6`](https://github.com/Rebekah-Chuang/VizAble/commit/2c74cb6b33fdc37fd8516dc761c211c159f62d27))

* Merge pull request #70 from Rebekah-Chuang:Rebekah-Chuang/issue69

docs: modify the docstring in `functions.py` by using the autoDocstring - Python Docstring Generator extension ([`445b865`](https://github.com/Rebekah-Chuang/VizAble/commit/445b865e6fc1d3fdbd7868674127df2c17853457))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue69 ([`d5b81d5`](https://github.com/Rebekah-Chuang/VizAble/commit/d5b81d5d74668bd4ee58e470792f0d00b896a05d))

* Merge pull request #68 from Rebekah-Chuang:Rebekah-Chuang/issue67

chore: add Github actions set up `.github/workflows/pytest.yaml` ([`6fcda19`](https://github.com/Rebekah-Chuang/VizAble/commit/6fcda19dc38fe8f22a6b53ced48fd65452d05df7))

* Merge remote-tracking branch &#39;origin/main&#39; into Rebekah-Chuang/issue67 ([`087b967`](https://github.com/Rebekah-Chuang/VizAble/commit/087b9676e1e20c75fd96e340470e0f8242618810))

* Merge pull request #66 from Rebekah-Chuang:Rebekah-Chuang/issue65

docs: add type annotations for functions in `app.py/server()` ([`f760911`](https://github.com/Rebekah-Chuang/VizAble/commit/f76091164f610ab98205a3f5de4648b16b5723cd))

* Merge pull request #63 from Rebekah-Chuang:Rebekah-Chuang/issue62

doc: add type annotation for functions in `functions.py` ([`b504d86`](https://github.com/Rebekah-Chuang/VizAble/commit/b504d86657cac62ca46c61e01929346c21ff9488))

* Merge pull request #61 from Rebekah-Chuang:Rebekah-Chuang/issue60

fix(accessibility): add header landmark for panel title on each page ([`ccd7c40`](https://github.com/Rebekah-Chuang/VizAble/commit/ccd7c40f802eb93f33088f93f003a7dbd83675da))

* Merge pull request #59 from Rebekah-Chuang:Rebekah-Chuang/issue42

fix(accessibility): add one main landmark for each tab ([`9f82997`](https://github.com/Rebekah-Chuang/VizAble/commit/9f829973ed0b3700c94e1f04a1752dfb3b0d7ab9))

* Merge pull request #56 from Rebekah-Chuang:Rebekah-Chuang/issue55

test: add unit test for `functions.py/get_excel_sheet_names()` ([`a2e45e8`](https://github.com/Rebekah-Chuang/VizAble/commit/a2e45e8e5e8521b79c0f1547338b9bd76edc9622))

* Merge pull request #54 from Rebekah-Chuang:Rebekah-Chuang/issue53

refactor: move `test_dataframe` folder to `tests` folder for better organization ([`611a2d5`](https://github.com/Rebekah-Chuang/VizAble/commit/611a2d5cd71d7aebddbac57f06bd7517183a7098))

* Merge pull request #52 from Rebekah-Chuang:Rebekah-Chuang/issue51

refactor: move `get_excel_sheet_names()` into `functions.py` for better unit testing ([`71ac64d`](https://github.com/Rebekah-Chuang/VizAble/commit/71ac64de7f46089cc04d5f75bfd6e6bb6e00a2fd))

* Merge pull request #50 from Rebekah-Chuang:Rebekah-Chuang/issue49

Update test_get_file_id() in tests/test_functions.py ([`868cc74`](https://github.com/Rebekah-Chuang/VizAble/commit/868cc747aac7f286803ddb9071b2093bd5a82f26))

* Merge pull request #47 from Rebekah-Chuang:Rebekah-Chuang/issue45

chore: use `poetry` package for better package maintenance ([`cd758df`](https://github.com/Rebekah-Chuang/VizAble/commit/cd758dfd80df004979939c369845f3e43039c2ab))

* Merge pull request #44 from Rebekah-Chuang:Rebekah-Chuang/issue43

test: add unit test for `functions.py/get_file_id()` ([`d7dadcc`](https://github.com/Rebekah-Chuang/VizAble/commit/d7dadcc3d89cbfbc1aee3980d0506d918c273618))

* Merge pull request #38 from Rebekah-Chuang:Rebekah-Chuang/issue37

fix(accessibility): the &lt;html&gt; element does not have a lang attribute ([`afd6aa5`](https://github.com/Rebekah-Chuang/VizAble/commit/afd6aa542f9fe6bc9008860a668beaf08d3e22bc))

* Merge pull request #40 from Rebekah-Chuang:Rebekah-Chuang/issue39

fix(accessibility): missing level-one heading in `app.py` ([`ed3aeac`](https://github.com/Rebekah-Chuang/VizAble/commit/ed3aeac10f9a60264d793ea0ee1cac57a5a235e0))

* Merge pull request #35 from Rebekah-Chuang:Rebekah-Chuang/issue28

fix: error occurred when uploading file without selecting plot type ([`2b7e8f1`](https://github.com/Rebekah-Chuang/VizAble/commit/2b7e8f100fedf23d3e479216ed782bd849d27128))

* Merge pull request #32 from Rebekah-Chuang:Rebekah-Chuang/issue31

fix: Fix plot types dropdown not resetting ([`827f530`](https://github.com/Rebekah-Chuang/VizAble/commit/827f530d4d1ec624a2f976bab9dd0ba703761ac8))

* Merge pull request #30 from Rebekah-Chuang:Rebekah-Chuang/issue29

fix: Fix issue with automatic data type conversion in DataFrame ([`a18388d`](https://github.com/Rebekah-Chuang/VizAble/commit/a18388df38a3a6741a837a9e3182d0dd239320f6))

* Merge pull request #27 from Rebekah-Chuang:Rebekah-Chuang/issue20

Add dropdown to display sheet names for uploaded Excel files ([`fb63761`](https://github.com/Rebekah-Chuang/VizAble/commit/fb63761836041abb5a1e034d0b82b11436255b49))

* Merge pull request #26 from Rebekah-Chuang:Rebekah-Chuang/issue25

Add error handling for unsuccessful column conversion ([`59646d3`](https://github.com/Rebekah-Chuang/VizAble/commit/59646d355e615b257a2c2db87bc38804b869a12e))

* Merge pull request #24 from Rebekah-Chuang:Rebekah-Chuang/issue23

Fix dataframe column data type conversion ([`08f609e`](https://github.com/Rebekah-Chuang/VizAble/commit/08f609e3f15a72be50efdb98d8ffabee05fb7004))

* update `CHANGELOG.md` ([`e4ed4f8`](https://github.com/Rebekah-Chuang/VizAble/commit/e4ed4f8c22028a2efa16d0fc6862f8c4290136ef))

* Merge pull request #22 from Rebekah-Chuang:Rebekah-Chuang/issue19

Display datatypes when uploading files ([`17dfb3b`](https://github.com/Rebekah-Chuang/VizAble/commit/17dfb3bc2792869af8ff8de537709f742bd9f036))

* update `CHANGELOG.md` ([`911471a`](https://github.com/Rebekah-Chuang/VizAble/commit/911471a5768d1e285b7f98bb5386ff54c9e523b2))

* Display datatypes to user when uploading files ([`28ce413`](https://github.com/Rebekah-Chuang/VizAble/commit/28ce41356244727bdc30512b3293ad4971a294d7))

* Merge pull request #21 from Rebekah-Chuang:Rebekah-Chuang/issue13

feat: Add dropdowns for selecting x-axis and y-axis columns ([`b2b12b8`](https://github.com/Rebekah-Chuang/VizAble/commit/b2b12b8fc5a750c5648eec2ef5a5094240d88b27))

* Update `output_dataframe` to return DataGrid with filters ([`3fd75e8`](https://github.com/Rebekah-Chuang/VizAble/commit/3fd75e89e24274aee214462f9d33cb36c2fbad5d))

* Add a dropdown for users to select columns when choosing line plot
Fixes #13 ([`7715193`](https://github.com/Rebekah-Chuang/VizAble/commit/7715193397b2277873e9e774ddc476b38cec0d9c))

* Merge pull request #12 from Rebekah-Chuang:Rebekah-Chuang/issue9

feat: Added introductions for different plot types based on user selection ([`84c51c7`](https://github.com/Rebekah-Chuang/VizAble/commit/84c51c70ba2ac8e87d5364afdf7f3df46681d18d))

* Merge pull request #10 from Rebekah-Chuang:Rebekah-Chuang/issue8

Add  a dropdown for users to select different plot types ([`e420977`](https://github.com/Rebekah-Chuang/VizAble/commit/e420977421e847d3fa3d1bcbbdb2e1ca4a224c7e))

* Add  a dropdown for users to select different plot types
Fixes #8 ([`bbf12d9`](https://github.com/Rebekah-Chuang/VizAble/commit/bbf12d99d34232a90d927380f8e726acc41d3732))

* Merge pull request #7 from Rebekah-Chuang:Rebekah-Chuang/issue5

Add navigation tabs/pages for different steps of the process ([`14a82e8`](https://github.com/Rebekah-Chuang/VizAble/commit/14a82e82c07b35c22505730680e199cf805139ac))

* Add navigation tabs/pages for different steps of the process
Fixes #5 ([`d0b6dbe`](https://github.com/Rebekah-Chuang/VizAble/commit/d0b6dbe72c22b6e3e8d9973dc1c1983ec33196d5))

* delete duplicated files in a directory tree &amp; fix typo ([`b42dff4`](https://github.com/Rebekah-Chuang/VizAble/commit/b42dff4f5bd989b9811c3b432e7ec96e1995aa4c))

* Merge pull request #4 from Rebekah-Chuang:Rebekah-Chuang/issue3

Add a dropdown to allow different file formats (.csv, .tsv, .xlsx). ([`eb57b4b`](https://github.com/Rebekah-Chuang/VizAble/commit/eb57b4be3cfbb74ada4bc9143effe57cc00b21b4))

* change folder name from `.shiny` to `apps` ([`24290f0`](https://github.com/Rebekah-Chuang/VizAble/commit/24290f0c7caa1189d48fd8148d4d43900ffb07c5))

* add `./shiny/` folder ([`ec0956f`](https://github.com/Rebekah-Chuang/VizAble/commit/ec0956fb7b1e0deb1a572d42f8e19019ad362a31))

* Add a dropdown to allow different file formats (.csv, .tsv, .xlsx).
Fixes #3 ([`86d6136`](https://github.com/Rebekah-Chuang/VizAble/commit/86d6136725a18f370f07e533d93aa15e9e9c38ba))

* Merge pull request #2 from Rebekah-Chuang/Rebekah-Chuang/issue1 ([`8e62e9b`](https://github.com/Rebekah-Chuang/VizAble/commit/8e62e9bf64e09137b348067c8f1e3ef791debceb))

* Add CHANGELOG.md
Fixes #1 ([`126d63f`](https://github.com/Rebekah-Chuang/VizAble/commit/126d63ffa1d60b0ad3957113a061248df264c36b))

* upload `requirements.txt` ([`263bed9`](https://github.com/Rebekah-Chuang/VizAble/commit/263bed9a4c3c39d639935d32e72bcea36ca13666))

* update format ([`97c5892`](https://github.com/Rebekah-Chuang/VizAble/commit/97c5892bf0d1a0a261346fe5aba0a8be706076bf))

* try shiny `@render.dataframe` ([`d03897c`](https://github.com/Rebekah-Chuang/VizAble/commit/d03897c14492a4a807b7a0200957f838ed3da96f))

* updated app.py ([`d6ba369`](https://github.com/Rebekah-Chuang/VizAble/commit/d6ba3698dd44145ee66b66b11e753826686b89ff))

* move file ([`7e33f3c`](https://github.com/Rebekah-Chuang/VizAble/commit/7e33f3ce87a74dd58d6f1d193cd19230c4ee1890))

* update `tab_header` in gt ([`caa9f65`](https://github.com/Rebekah-Chuang/VizAble/commit/caa9f6536f0831bc8899e2423c4159ee608b548b))

* render table using great_tables ([`0b1785a`](https://github.com/Rebekah-Chuang/VizAble/commit/0b1785abf74c48eac3ad0056599814325a904d57))

* generate test dataframe ([`a0b50a0`](https://github.com/Rebekah-Chuang/VizAble/commit/a0b50a0723611c2340bdfc6c4cdc231f898f88a9))

* upload file features ([`70ef048`](https://github.com/Rebekah-Chuang/VizAble/commit/70ef048d4839caeaaaddd6812fda1d6c68880c4f))

* create initial app ([`762ec63`](https://github.com/Rebekah-Chuang/VizAble/commit/762ec63fb0e3da8dab65cec855a0f0cf06a38d46))

* Initial commit ([`a3ae0f3`](https://github.com/Rebekah-Chuang/VizAble/commit/a3ae0f3ceee1a0268e36c3dfaeeeb61de75dd5d8))

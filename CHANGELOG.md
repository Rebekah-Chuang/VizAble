# CHANGELOG



## v0.7.0 (2024-03-31)

### Chore

* chore: trigger shinyappsio-deployment workflow on new github release ([`fa30fac`](https://github.com/Rebekah-Chuang/VizAble/commit/fa30fac2afdb4be450ced0ca30b843ff4ac8fe3c))

* chore: generate `requirements.txt` to workflow or deployment might fail ([`bca613f`](https://github.com/Rebekah-Chuang/VizAble/commit/bca613f3b27eed8a77388b42b5382309037a4d98))

* chore: remove pip install -r requirements.txt[skip ci] ([`768f5ea`](https://github.com/Rebekah-Chuang/VizAble/commit/768f5eab6abea9922357fdc6326d38e6a2627ed3))

* chore: update app path in shinyappsio-deployment workflow ([`e179bd7`](https://github.com/Rebekah-Chuang/VizAble/commit/e179bd787df7cb76938b46287669e11d9e89baa0))

* chore: run shinyappsio-deployment workflow without creating virtual env[skip ci] ([`f03bbd5`](https://github.com/Rebekah-Chuang/VizAble/commit/f03bbd576ce9a64f351a1b7c97b8ad0a810d97ce))

* chore: remove poetry shell due to github action&#39;s non-interactive environment[skip ci] ([`cc8a596`](https://github.com/Rebekah-Chuang/VizAble/commit/cc8a5960de44f9812eb8608333982ddef40d672b))

* chore: disable the interactive shell feature of Poetry[skip ci] ([`1299bce`](https://github.com/Rebekah-Chuang/VizAble/commit/1299bce8317a74b55d5ca1a6cd67a63763d8a4a9))

* chore: create virtual environment and save cache using poetry[skip ci] ([`033426c`](https://github.com/Rebekah-Chuang/VizAble/commit/033426c2134601a089e13b0a89483cb3a2d1aa1f))

* chore: add a step to install dependencies with poetry[skip ci] ([`ba16f0d`](https://github.com/Rebekah-Chuang/VizAble/commit/ba16f0d9bdf262f1dc443809d141b8075a23236f))

* chore: fix app path and use poetry for deployment ([`4762927`](https://github.com/Rebekah-Chuang/VizAble/commit/476292790b43076b78a350415b416939c5317e82))

* chore: fix app path for shinyappsio-deployment[skip ci] ([`5076ee5`](https://github.com/Rebekah-Chuang/VizAble/commit/5076ee58bc56309d69571a9699578aaa5aca8704))

* chore: install rsconnect-python using pip in shinyappsio-deployment workflow[skip ci] ([`f4b013c`](https://github.com/Rebekah-Chuang/VizAble/commit/f4b013c126f39c92a86235f8aff811cab673285b))

* chore: add GitHub Actions workflow for deploying app to shinyapps.io ([`39e383d`](https://github.com/Rebekah-Chuang/VizAble/commit/39e383d025f09ae510c864844307462f865798a0))

### Feature

* feat: add a feature to generate bar plot ([`a0fecab`](https://github.com/Rebekah-Chuang/VizAble/commit/a0fecabc74779bdf7ca6d60ca426c6ea2e09f42c))

* feat: add a feature to generate scatter plot ([`39481c9`](https://github.com/Rebekah-Chuang/VizAble/commit/39481c92df808e8e7ef49adea448572d25bac875))

### Test

* test: add dataframe to test scatter plot ([`03ed506`](https://github.com/Rebekah-Chuang/VizAble/commit/03ed506dd3c4eb90bf9217ecb8f10828b79bbccb))


## v0.6.0 (2024-03-28)

### Chore

* chore: trigger python-semantic-release every three days at 00:00 EST(05:00 UTC) ([`f522179`](https://github.com/Rebekah-Chuang/VizAble/commit/f5221798e6e28ad95c69416d6c96715063a64993))

* chore: add `shinywidgets` and `plotly` to project for generating plots ([`a093934`](https://github.com/Rebekah-Chuang/VizAble/commit/a093934e7787bb870f1880453090e2d82fafaf79))

### Documentation

* docs: update `README.md` with link to shinyapps.io ([`55ddf64`](https://github.com/Rebekah-Chuang/VizAble/commit/55ddf64b534b9c374c3b2754c980a5addd87715a))

### Feature

* feat: add line plot example ([`eec029e`](https://github.com/Rebekah-Chuang/VizAble/commit/eec029ebdb04c5c6cce800984c220f463b594451))


## v0.5.6 (2024-03-28)

### Build

* build: deploy app to shinyapps.io ([`020d72a`](https://github.com/Rebekah-Chuang/VizAble/commit/020d72a9ebd848227239428d42e63411371d327e))

### Chore

* chore: modify python version for deployment ([`ed5aef1`](https://github.com/Rebekah-Chuang/VizAble/commit/ed5aef1261f41ec8322320ceee41878e7d262472))

### Fix

* fix: allow users to reset all selections and input file by clicking reset button ([`37d715d`](https://github.com/Rebekah-Chuang/VizAble/commit/37d715dea260c45b59487b4a8c026412b42f1932))


## v0.5.5 (2024-03-13)

### Chore

* chore: add comments to workflows ([`ca698cf`](https://github.com/Rebekah-Chuang/VizAble/commit/ca698cf9b3d2b996d80c5bb7201f91babe683072))

* chore: update `exclude_commit_patterns` ro ignore specific commit patterns [skip ci] ([`2d1eabe`](https://github.com/Rebekah-Chuang/VizAble/commit/2d1eabe726493a8ba51a74f3412f8263c5351a94))

### Documentation

* docs: update badges with new links [skip ci] ([`6907e64`](https://github.com/Rebekah-Chuang/VizAble/commit/6907e64b2e4c63e34c7b1ae0b2e57a830611009c))

* docs: update badges in `README.md` with links ([`52a72cb`](https://github.com/Rebekah-Chuang/VizAble/commit/52a72cb087b7827947ac181d5fb7384a6805f0cf))

* docs: add badges to `README.md` ([`abf121f`](https://github.com/Rebekah-Chuang/VizAble/commit/abf121f2109de2fb148d3b1bde3281358026fb29))

* docs: update `CHANGELOG.md` [skip ci] ([`e4e661b`](https://github.com/Rebekah-Chuang/VizAble/commit/e4e661b5b94631872d24c11c2769710a11c6d2ed))

### Fix

* fix(accessibility): increase each heading by only one level at a time to improve accessibility ([`27236a2`](https://github.com/Rebekah-Chuang/VizAble/commit/27236a29a46d348f6710c53049e43e18a7b9ade0))


## v0.5.4 (2024-03-07)

### Ci

* ci: trigger publish to PyPI workflow when releasing [skip ci] ([`560cc30`](https://github.com/Rebekah-Chuang/VizAble/commit/560cc3072da9ff6c1cfda63a8fdfe120b823e866))

### Fix

* fix: modify instructions in home page [skip ci] ([`6a57f60`](https://github.com/Rebekah-Chuang/VizAble/commit/6a57f60636db1754b61cfd8db2cd2b1d0eec4b59))

### Unknown

* 0.5.4

Automatically generated by python-semantic-release ([`a8e829b`](https://github.com/Rebekah-Chuang/VizAble/commit/a8e829b62074a25f583839bf9c3d127fd5db7f32))


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

### Unknown

* 0.5.3

Automatically generated by python-semantic-release ([`46216b9`](https://github.com/Rebekah-Chuang/VizAble/commit/46216b94546cf73137d78c1598e37648d67f8967))


## v0.5.2 (2024-03-07)

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

* update `CHANGELOG.md` ([`e4ed4f8`](https://github.com/Rebekah-Chuang/VizAble/commit/e4ed4f8c22028a2efa16d0fc6862f8c4290136ef))

* update `CHANGELOG.md` ([`911471a`](https://github.com/Rebekah-Chuang/VizAble/commit/911471a5768d1e285b7f98bb5386ff54c9e523b2))

* Display datatypes to user when uploading files ([`28ce413`](https://github.com/Rebekah-Chuang/VizAble/commit/28ce41356244727bdc30512b3293ad4971a294d7))

* Update `output_dataframe` to return DataGrid with filters ([`3fd75e8`](https://github.com/Rebekah-Chuang/VizAble/commit/3fd75e89e24274aee214462f9d33cb36c2fbad5d))

* Add a dropdown for users to select columns when choosing line plot
Fixes #13 ([`7715193`](https://github.com/Rebekah-Chuang/VizAble/commit/7715193397b2277873e9e774ddc476b38cec0d9c))

* Add  a dropdown for users to select different plot types
Fixes #8 ([`bbf12d9`](https://github.com/Rebekah-Chuang/VizAble/commit/bbf12d99d34232a90d927380f8e726acc41d3732))

* Add navigation tabs/pages for different steps of the process
Fixes #5 ([`d0b6dbe`](https://github.com/Rebekah-Chuang/VizAble/commit/d0b6dbe72c22b6e3e8d9973dc1c1983ec33196d5))

* delete duplicated files in a directory tree &amp; fix typo ([`b42dff4`](https://github.com/Rebekah-Chuang/VizAble/commit/b42dff4f5bd989b9811c3b432e7ec96e1995aa4c))

* change folder name from `.shiny` to `apps` ([`24290f0`](https://github.com/Rebekah-Chuang/VizAble/commit/24290f0c7caa1189d48fd8148d4d43900ffb07c5))

* add `./shiny/` folder ([`ec0956f`](https://github.com/Rebekah-Chuang/VizAble/commit/ec0956fb7b1e0deb1a572d42f8e19019ad362a31))

* Add a dropdown to allow different file formats (.csv, .tsv, .xlsx).
Fixes #3 ([`86d6136`](https://github.com/Rebekah-Chuang/VizAble/commit/86d6136725a18f370f07e533d93aa15e9e9c38ba))

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

# Great Expectations
 > [Great Expectations](https://greatexpectations.io/) is the leading tool for validating, documenting, and profiling your data to maintain quality and improve communication between teams

# Features
* __Automated data profiling__ <br>
The library profiles your data to get basic statistics, and automatically generates a suite of Expectations based on what is observed in the data.
* __Data validation__ <br>
Expectation Suite passes or fails, and returns any unexpected values that failed a test
* __Data Docs__ <br>
Renders HTML file of Expectations in clean, human-readable documentation containing both Expectation Suites and data Validation Results
* __Diverse Datasources and Store backends__ <br>
Various datasources such Pandas dataframes, Spark dataframes, and SQL databases via SQLAlchemy.

# Overview

1. **Expectations suite json**
    * [faa_registration](/great-expectation/great_expectations/expectations/faa_registration_suite.json)
2. **Data Docs html report**
    * [faa_registration](/great-expectation/great_expectations/uncommitted/data_docs/local_site/expectations/faa_registration_suite.html)
3. **Validation run report**
    * [Home](/great_expectations/uncommitted/data_docs/local_site/index.html)
    * [faa_registration](/great_expectations/uncommitted/data_docs/local_site/validations/faa_registration_suite/20220611-035453-my-run-name-template/20220611T035453.307561Z/8832c98c74b764de338364367929a651.html)

## Dataset
  * [faa_registration.csv](/great_expectations/great_expectations/data/faa_registration.csv)
  * [Data Dictionary – FAA Registry](https://www.faa.gov/sites/faa.gov/files/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download/ardata.pdf)

---

Refer: [Getting started with Great Expectations](https://docs.greatexpectations.io/docs/tutorials/getting_started/tutorial_overview)

# Step 01: Environment Configuration

## 1.0 Create a python environment and activate it

## 1.1. Install module `great_expectations`
```bash
pip install great_expectations
```
## 1.2. Verify the version
```bash
great_expectations --version
```
Output: `great_expectations, version 0.15.46`
## 03. Initialize at the base dir
```bash
great_expectations init
```
Change working dir to the newly created dir, `great_expectations`
```bash
cd great_expectations
```
## 04. Import data into repo
Copy the csv into `great_expectations/data`
Files:
> faa_registration.csv


# Step 02: Connect to data
## 05. Launch cli datasource process
```bash
great_expectations datasource new
```
Input following in the prompt
> `1` - Local File<br> `1` - Pandas <br> `data` - relative path to datasets

This open a Jupyter notebook, <br>
* Change to `datasource_name` var to `nyc_yellow_taxi_trip_data`
* Update `example_yaml` to ignore all non csv files
    ```python
    example_yaml = f"""
    name: {datasource_name}
    class_name: Datasource
    execution_engine:
      class_name: PandasExecutionEngine
    data_connectors:
      default_inferred_data_connector_name:
        class_name: InferredAssetFilesystemDataConnector
        base_directory: data
        default_regex:
          group_names:
            - data_asset_name
          pattern: (.*)
      default_runtime_data_connector_name:
        class_name: RuntimeDataConnector
        assets:
          my_runtime_asset_name:
            batch_identifiers:
              - runtime_batch_identifier_name
    """
    print(example_yaml)
    ```
* Save the datasource Configuration
* Close Jupyter notebook
* Wait for terminal to show `Saving file at /datasource_new.ipynb`

# Step 03: Create Expectations for nyc_yellow_taxi_trip_data

## 3.1. Launch cli suite process
```bash
great_expectations suite new
```
Input following in the prompt
  > `3` - Automatically, using a profiler <br> `1` - Select index of file `faa_registration.csv` <br> `faa_registration_suite` - suite name

This open a Jupyter notebook, <br>
* Change to `datasource_name` var to `spy_plane_data`
* Update `exclude_column_names` to
    ```python
    exclude_column_names = [
        "N-NUMBER",
        "SERIAL NUMBER",
        "MFR MDL CODE",
        "ENG MFR MDL",
    #    "YEAR MFR",
        "TYPE REGISTRANT",
        "NAME",
        "STREET",
        "STREET2",
        "CITY",
        "STATE",
        "ZIP CODE",
        "REGION",
        "COUNTY",
        "COUNTRY",
    #    "LAST ACTION DATE",
    #    "CERT ISSUE DATE",
        "CERTIFICATION",
        "TYPE AIRCRAFT",
        "TYPE ENGINE",
        "STATUS CODE",
        "MODE S CODE",
        "FRACT OWNER",
        "AIR WORTH DATE",
        "OTHER NAMES(1)",
        "OTHER NAMES(2)",
        "OTHER NAMES(3)",
        "OTHER NAMES(4)",
        "OTHER NAMES(5)",
    #    "EXPIRATION DATE",
    #    "UNIQUE ID",
        "KIT MFR",
        "KIT MODEL",
        "MODE S CODE HEX",
        "X35",
    ]
    ```
* Run to create default expectation and analyze the result
* Wait for terminal to show  `Saving file at /*.ipynb`
* Modify expectation as per need <br>
    Modified the JSON file `great_expectations/expectations/faa_registration_suite.json` and kept necessary expectations <br>

    ```bash
    great_expectations suite edit faa_registration_suite
    ```
    Input following in the prompt (! SYS ERROR, COULD NOT LOAD THE NOTEBOOK)
  > `1` - Manually, without interacting with a sample batch of data (default)

  
  Updated to: <br>
  `This Expectation suite currently contains 4 total Expectations across 1 columns.`

# Step 04: Validate Data
## 4.1. Create checkpoint
```bash
great_expectations checkpoint new planes_features_checkpoint_v0.1
```

  This open a Jupyter notebook, <br>

* Run all cells.
* Report in new page

# Step 05: Commit the following files and folders 
* great_expectations/data
* great_expectations/expectations/*.json
* great_expectations/uncommitted/data_docs/*
* great_expectations/uncommitted/*.ipynb

  Resource: https://git-scm.com/docs/gitignore

# Step 06: Deploying using Git Actions

# Ends
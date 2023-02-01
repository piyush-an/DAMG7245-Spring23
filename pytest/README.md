# Pytest

The [pytest](https://docs.pytest.org/en/7.2.x/contents.html) framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

## Tutorials

1. Install package
    ```bash
    pip install pytest
    ```

2. Create test

    * Create a new file called [test.py](test.py), containing test
    * Test function should start with `test_*`

3. Run tests
    ```bash
    pytest -v test.py
    ```

4. Export Result to a file
    ```bash
    pytest -v test.py > test_run_$(date "+%Y-%m-%d_%H:%M:%S").log
    ```

    Sample test result [pytest/test_run_2023-02-01_17:59:40.log](test_run_2023-02-01_17:59:40.log)


Additional:

Implement Unit testing with Git Actions as CI

* Git Actions file defined [pytest.yml](/.github/workflows/pytest.yml)
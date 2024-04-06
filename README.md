## Installing dependencies

To install the necessary dependencies, follow these steps:

1. Open your terminal.

2. Move to the `FASEP` folder using the command :

   ```
   cd path/to/FASEP
   ```

3. Run the following command to install dependencies from the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

## Running tests

Once installation is complete, proceed as follows to run tests:

1. Move to the `tests` folder:

   ```
   cd tests
   ```

2. In the `test.py` file, replace the path contained in the `test_file_path` variable with 

the path to the file `Example FASEP.pptx` on your computer. (You may need to change the "/" to "\").

Save your changes.

3. Run the tests using `pytest` :

   ```
   pytest test.py
   ```


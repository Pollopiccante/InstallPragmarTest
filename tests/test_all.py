import os
import shutil
import unittest

from PRAGMAR.main import load_all_parent

def delete_files_in_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def test_scenario(test_name):
    load_all_parent(f"tests.{test_name}.def", f"tests.{test_name}.gen")

class TestAll(unittest.TestCase):
    def test_most_specific_inheritor(self):
        test_scenario("closest_inheritor")

    def test_closest_inheritor(self):
        test_scenario("closest_inheritor")

    def test_inherit_name_over_type(self):
        test_scenario("closest_inheritor")

    def test_multible_aspect_files(self):
        test_scenario("multible_aspect_files")

    def test_optional_field_files(self):
        test_scenario("optional_field")

    def test_runtime_only(self):
        from tests.runtime_only.single_file import run
        run()









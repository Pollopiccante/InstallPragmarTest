import os
import shutil
import unittest


def scenario(test_function):
    def out_function(self):
        scenario_name = test_function.__name__.replace("test_", "")
        runner = ScenarioRunner("tests/" + scenario_name)
        test_function(self, runner)
    return out_function

class ScenarioRunner:
    def __init__(self, directory_path):
        self._directory_path = directory_path
        self.grammar_subpath = self._directory_path + "/grammar.py"
        self.attributes_subpath = self._directory_path + "/attributes.py"
        self.use_subpath = self._directory_path + "/use.py"
        self.gen_directory = self._directory_path + "/gen/"

    def delete_generated_files(self):
        print(f"    DELETING FILES IN: {self.gen_directory}")
        delete_files_in_folder(self.gen_directory)

    def run_grammar(self):
        print(f"    RUNNING Grammar: {self.grammar_subpath}")
        return run_python_file(self.grammar_subpath)

    def run_attributes(self):
        print(f"    RUNNING Attributes: {self.attributes_subpath}")
        return run_python_file(self.attributes_subpath)

    def run_use(self):
        print(f"    RUNNING Use: {self.use_subpath}")
        return run_python_file(self.use_subpath)

    def run_all(self):
        print(f"RUNNING SCENARIO: {self.gen_directory}")
        self.delete_generated_files()
        g = self.run_grammar()
        a = self.run_attributes()
        u = self.run_use()
        print(f"    OUTPUT: {g} {a} {u}")
        return [g, a, u]

    def check(self, asserter):
        grammar, attributes, use = self.run_all()
        asserter.assertEqual(0, grammar, "Grammar Generation did not succeed")
        asserter.assertEqual(0, attributes, "Attribute Generation did not succeed")
        asserter.assertEqual(0, use, "UseCase did not succeed")
        print(f"    SCENARIO passed")


def run_python_file(file_path: str) -> int:
    return os.system(f"python3 {file_path}")


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

class Tests(unittest.TestCase):
    @scenario
    def test_most_specific_inheritor(self, runner: ScenarioRunner):
        runner.check(self)

    @scenario
    def test_closest_inheritor(self, runner: ScenarioRunner):
        runner.check(self)

    @scenario
    def test_inherit_name_over_type(self, runner: ScenarioRunner):
        runner.check(self)









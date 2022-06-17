class LanguageHandler:
    def __init__(self, language, input_files, output_files, user_input):
        self.language = language
        self.input_files = input_files
        self.output_files = output_files
        self.user_input = user_input or None

    # Add a function which enforces execution of the language handler
    def execute(self):
        if self.user_input:
            self.execute_single()
        else:
            self.execute_batch()
        pass


# Inherit from LanguageHandler for python
class PythonHandler(LanguageHandler):
    def __init__(self, language, input_files, output_files, user_input):
        super().__init__(language, input_files, output_files, user_input)

    def execute(self):
        super().execute()

    def execute_single(self):
        # Execute the language handler
        print("Executing Single Python Handler")
        pass

    def execute_batch(self):
        print("Executing Batch Python Handler")
        pass


# Inherit from LanguageHandler for C
class CHandler(LanguageHandler):
    def __init__(self, language, input_files, output_files, user_input):
        super().__init__(language, input_files, output_files, user_input)

    def execute(self):
        super().execute()

    def execute_single(self):
        # Execute the language handler
        pass

    def execute_batch(self):
        # Execute the language handler
        pass


# Inherit from LanguageHandler for C++
class CppHandler(LanguageHandler):
    def __init__(self, language, input_files, output_files, user_input):
        super().__init__(language, input_files, output_files, user_input)

    def execute(self):
        super().execute()

    def execute_single(self):
        # Execute the language handler
        pass

    def execute_batch(self):
        # Execute the language handler
        pass


def get_language_handler(language, *args, **kwargs):
    if language == "python":
        return PythonHandler(language, *args, **kwargs)
    elif language == "c":
        return CHandler(language, *args, **kwargs)
    elif language == "cpp":
        return CppHandler(language, *args, **kwargs)
    else:
        raise Exception("Language not supported")
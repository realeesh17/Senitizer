class Sanitizer:
    def sanitize_input(self, user_input):
        """
        Cleans the user input by removing any unwanted characters.
        """
        # Example implementation: remove leading/trailing whitespace and HTML tags
        import re
        sanitized = re.sub(r'<.*?>', '', user_input).strip()
        return sanitized

    def validate_input(self, user_input):
        """
        Validates the User Inputs to ensure it meets certain criteria.
        """
        # Example implementation: check if INPUT is not empty and is alphanumeric.
        if not user_input or not user_input.isalnum():
            return False
        return True
import subprocess

class OllamaCore():
    _instance = None  # Singleton instance
    _model = "gemma:2b"  # Default model

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OllamaCore, cls).__new__(cls)
        return cls._instance

    @classmethod
    def set_model(cls, new_model):
        """Set the LLM model to use."""
        cls._model = new_model

    @classmethod
    def get_model(cls):
        """Get the current model name."""
        return cls._model

    @classmethod
    def run(cls, prompt):
        """Run the LLM model in Ollama."""
        result = subprocess.run(
            ["ollama", "run", cls._model, prompt],
            capture_output=True, text=True
        )
        return result.stdout.strip()

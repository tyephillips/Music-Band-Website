# Import the base AppConfig class from Django's apps module
from django.apps import AppConfig


class HorizonsConfig(AppConfig):
    """
    Configuration class for the 'horizons' Django application.
    
    This class is used to define application-specific settings, such as:
    - The default type of primary key field for models.
    - The name of the application.
    
    It is automatically referenced in the project's settings under INSTALLED_APPS.
    """
    # Set the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the name of the app, which matches the app directory name
    name = 'horizons'


"""
This module contains custom logger for tacking tenor of battle.
"""

from time import gmtime, strftime
from pathlib import Path

from constants import LOG_OUTPUT_DIR
from common_functions import create_directory
from structures_enums_classes import Singleton


class CustomLogger(metaclass=Singleton):
    """
    Custom logger without tracebacks, but to tracj tenor of battle.

    Fileds:
        self.file
    """

    internal_action_intend = '    '

    def __init__(self) -> None:
        self.log_file_name = self._get_new_log_path()

    @staticmethod
    def _get_new_log_path() -> Path:
        """Method to craete log path.

        This method creates path for new log file based on current timestamp.

        Retruns:
            Path: Path to new log file.
        """
        create_directory(LOG_OUTPUT_DIR)
        timestamp = strftime('%Y-%m-%d_%H-%M-%S', gmtime())
        new_log_name = f'{timestamp}.log'
        return Path(LOG_OUTPUT_DIR, new_log_name)

    def _save_message_to_log(self, message: str, empty_line=False) -> None:
        """Method to save any kind of message to log file.

        This method saves messages to active log file.
        Message should be prepared by other methods.

        Args:
            message (str): Message to send.
            empty_line (boolean): Information if empty line before message should be created (without timestamp).
        """
        timestamp = strftime('%H:%M:%S')
        log_msg = f'{timestamp} {message}'
        with open(file=self.log_file_name, mode='a', encoding='ustf-8') as file:
            if empty_line:
                file.write('\n')
            file.write(log_msg)

    def save_internal_action(self, message: str, intend_number=1) -> None:
        """Method saves internal action.

        This method saves given message as internal action.
        Internal action is saved with intends.

        Args:
            message (str): Message to save.
            intend_number (int): Number of standard intends.
        """
        # TODO
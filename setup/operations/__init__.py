"""
Super-OpenCode Operations Module

This module contains all Super-OpenCode management operations that can be
executed through the unified CLI hub (Super-OpenCode.py).

Each operation module should implement:
- register_parser(subparsers): Register CLI arguments for the operation
- run(args): Execute the operation with parsed arguments

Available operations:
- install: Install Super-OpenCode framework components
- update: Update existing Super-OpenCode installation
- uninstall: Remove Super-OpenCode framework installation  
- backup: Backup and restore Super-OpenCode installations
"""

__version__ = "3.0.0"
__all__ = ["install", "update", "uninstall", "backup"]


def get_operation_info():
    """Get information about available operations"""
    return {
        "install": {
            "name": "install",
            "description": "Install Super-OpenCode framework components",
            "module": "setup.operations.install"
        },
        "update": {
            "name": "update", 
            "description": "Update existing Super-OpenCode installation",
            "module": "setup.operations.update"
        },
        "uninstall": {
            "name": "uninstall",
            "description": "Remove Super-OpenCode framework installation", 
            "module": "setup.operations.uninstall"
        },
        "backup": {
            "name": "backup",
            "description": "Backup and restore Super-OpenCode installations",
            "module": "setup.operations.backup"
        }
    }


class OperationBase:
    """Base class for all operations providing common functionality"""
    
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.logger = None
    
    def setup_operation_logging(self, args):
        """Setup operation-specific logging"""
        from ..utils.logger import get_logger
        self.logger = get_logger()
        self.logger.info(f"Starting {self.operation_name} operation")
    
    def validate_global_args(self, args):
        """Validate global arguments common to all operations"""
        errors = []
        
        # Validate install directory
        if hasattr(args, 'install_dir') and args.install_dir:
            from ..utils.security import SecurityValidator
            is_safe, validation_errors = SecurityValidator.validate_installation_target(args.install_dir)
            if not is_safe:
                errors.extend(validation_errors)
        
        # Check for conflicting flags
        if hasattr(args, 'verbose') and hasattr(args, 'quiet'):
            if args.verbose and args.quiet:
                errors.append("Cannot specify both --verbose and --quiet")
        
        return len(errors) == 0, errors
    
    def handle_operation_error(self, operation: str, error: Exception):
        """Standard error handling for operations"""
        if self.logger:
            self.logger.exception(f"Error in {operation} operation: {error}")
        else:
            print(f"Error in {operation} operation: {error}")
        return 1
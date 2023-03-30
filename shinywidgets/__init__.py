"""Top-level package for shinywidgets."""

__author__ = """Carson Sievert"""
__email__ = "carson@rstudio.com"
__version__ = "0.1.6.9000"

from ._dependencies import bokeh_dependency
from ._shinywidgets import output_widget, reactive_read, register_widget, render_widget

__all__ = ("output_widget", "register_widget", "render_widget", "reactive_read", "bokeh_dependency")

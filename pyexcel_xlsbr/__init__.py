"""
    pyexcel_xlsbr
    ~~~~~~~~~~~~~~~~~~~
    The lower level xlsb file format handler
    :copyright: (c) 2018 by Onni Software Ltd & its contributors
    :license: New BSD License
"""
# flake8: noqa
from pyexcel_io.io import get_data as read_data
from pyexcel_io.io import isstream
from pyexcel_io.plugins import IOPluginInfoChain

from ._version import __author__, __version__

__FILE_TYPE__ = "xlsb"

IOPluginInfoChain(__name__).add_a_reader(
    relative_plugin_class_path="xlsbr.XLSBBook",
    file_types=[__FILE_TYPE__],
    stream_type="binary",
)


def get_data(afile, file_type=None, **keywords):
    """standalone module function for reading module supported file type"""
    if isstream(afile) and file_type is None:
        file_type = __FILE_TYPE__
    return read_data(afile, file_type=file_type, **keywords)

"""This is the Bokeh charts interface. It gives you a high level API to build
complex plot is a simple way.

This is the BoxPlot class which lets you build your BoxPlot plots just passing
the arguments to the Chart class and calling the proper functions.
It also add a new chained stacked method.
"""
#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2014, Continuum Analytics, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from __future__ import absolute_import

from .._builder import create_and_build
from ...models import Range1d
from ...properties import Bool, String
from .bar_builder import BarBuilder
from ..glyphs import BoxGlyph

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------


def BoxPlot(data, label=None, values=None, color=None, group=None,
            xscale="categorical", yscale="linear", xgrid=False,
            ygrid=True, continuous_range=None, **kw):

    if continuous_range and not isinstance(continuous_range, Range1d):
        raise ValueError(
            "continuous_range must be an instance of bokeh.models.ranges.Range1d"
        )

    # The continuous_range is the y_range (until we implement HBar charts)
    y_range = continuous_range
    kw['label'] = label
    kw['values'] = values
    kw['color'] = color
    kw['group'] = group
    kw['xscale'] = xscale
    kw['yscale'] = yscale
    kw['xgrid'] = xgrid
    kw['ygrid'] = ygrid
    kw['y_range'] = y_range

    return create_and_build(BoxPlotBuilder, data, **kw)


class BoxPlotBuilder(BarBuilder):
    """This is the BoxPlot class and it is in charge of plotting
    scatter plots in an easy and intuitive way.

    Essentially, we provide a way to ingest the data, make the proper
    calculations and push the references into a source object.
    We additionally make calculations for the ranges.
    And finally add the needed glyphs (rects, lines and markers)
    taking the references from the source.

    """

    # TODO: (bev) should be an enumeration
    marker = String(help="""
    The marker type to use (e.g., ``circle``) if outliers=True.
    """)

    outliers = Bool(help="""
    Whether to display markers for any outliers.
    """)

    glyph = BoxGlyph
